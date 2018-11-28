#include <iostream>
#include <cstdio>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> v[155];
pair<int,int> grid[55][55]; //number, owner (row, col)
pair<int,int> taken[105]; //number, row(0)/col(1)
vector<int> rows;
vector<int> cols;
int n;
int sk=-1;
bool sktype=false; //false row, true col

bool fill_row(int vno, int row_num){ //False if not able to fill
	for (int i=0; i<n; i++){
		if (grid[row_num][i].second!=-1){ //Has been taken
			//Test if correct
			if (grid[row_num][i].first != v[vno][i]){
				return false;
			}
		}
		else{
			grid[row_num][i] = make_pair(v[vno][i],vno);
		}
	}
	return true;
}

void unfill_row(int vno, int row_num){
	for (int i=0; i<n; i++){
		if (grid[row_num][i].second==vno){ //Has been taken
			grid[row_num][i] = make_pair(-1,-1);
		}
	}
}

bool fill_col(int vno, int col_num){
	for (int i=0; i<n; i++){
		if (grid[i][col_num].second!=-1){ //Has been taken
			//Test if correct
			if (grid[i][col_num].first != v[vno][i]){
				return false;
			}
		}
		else{
			grid[i][col_num] = make_pair(v[vno][i],vno);
		}
	}
	return true;
}

void unfill_col(int vno, int col_num){
	for (int i=0; i<n; i++){
		if (grid[i][col_num].second==vno){ //Has been taken
			grid[i][col_num] = make_pair(-1,-1);
		}
	}
}

void print_grid(){
	for (int i=0; i<n; i++){
		for (int j=0; j<n; j++){
			cout << grid[i][j].first << " ";
		}
		cout << endl;
	}
}

int get_answer(int num_pos, bool skipped){ //number of positions filled, skipped or not 1 if pass, 0 if fail
	//cout << "num_pos: " << num_pos << " skipped: " << skipped << endl;
	//print_grid();
	if (num_pos==2*n-1){
		return 1;
	}
	//Suppose is row
	int row_num;
	if (rows.size()==0){
		row_num=0;
	}
	else{
		row_num=rows[rows.size()-1]+1;
	}
	if (row_num<n){
		rows.push_back(row_num);
		//Try to fill
		if (fill_row(num_pos,row_num)){
			if (get_answer(num_pos+1,skipped)==1){
				return 1;
			}
		}
		unfill_row(num_pos,row_num);
		rows.pop_back();
	}
	//Suppose is col
	int col_num;
	if (cols.size()==0){
		col_num=0;
	}
	else{
		col_num=cols[cols.size()-1]+1;
	}
	if (col_num<n){
		cols.push_back(col_num);
		//Try to fill
		if (fill_col(num_pos,col_num)){
			//cout << "num_pos: " << num_pos << " skipped: " << skipped << " could fill col" << endl;
			if (get_answer(num_pos+1,skipped)==1){
				return 1;
			}
		}
		/*else{
			cout << "num_pos: " << num_pos << " skipped: " << skipped << " could not fill col" << endl;
		}*/
		unfill_col(num_pos,col_num);
		cols.pop_back();
	}
	if (!skipped){
		row_num += 1;
		if (row_num<n){
			rows.push_back(row_num);
			//Try to fill
			if (fill_row(num_pos,row_num)){
				sk=row_num-1;
				sktype=false;
				if (get_answer(num_pos+1,true)==1){
					return 1;
				}
				sk=-1;
			}
			unfill_row(num_pos,row_num);
			rows.pop_back();
		}
		col_num += 1;
		if (col_num<n){
			cols.push_back(col_num);
			//Try to fill
			if (fill_col(num_pos,col_num)){
				sk=col_num-1;
				sktype=true;
				if (get_answer(num_pos+1,skipped)==1){
					return 1;
				}
				sk=-1;
			}
			unfill_col(num_pos,col_num);
			cols.pop_back();
		}
	}
	return 0;
}

int main(){
	ifstream fin("b.txt");
	ofstream fout("b_out.txt");
	int t;
	fin >> t;
	for (int i=0; i<t; i++){
		fin >> n;
		for (int j=0; j<2*n-1; j++){
			vector<int> tmp;
			int tmp2;
			for (int k=0; k<n; k++){
				fin >> tmp2;
				tmp.push_back(tmp2);
			}
			v[j]=tmp;
		}
		sort(v,v+2*n-1);
		/*for (int j=0; j<2*n-1; j++){
			for (int k=0; k<v[j].size(); k++){
				cout << v[j][k] << " ";
			}
			cout << endl;
		}*/
		for (int j=0; j<n; j++){
			for (int k=0; k<n; k++){
				grid[j][k]=make_pair(-1,-1);
			}
		}
		fout << "Case #" << i+1 << ": ";
		if (get_answer(0,false)){
			if (sk==-1){
				sk=n-1;
				if (rows.size()!=n){
					sktype=false;
				}
				else{
					sktype=true;
				}
			}
			//fout << " sk: " << sk << " sktype: " << sktype << " ";
			if (sktype==0){ //row
				for (int j=0; j<n; j++){
					if (j==n-1){
						fout << grid[sk][j].first << endl;
					}
					else{
						fout << grid[sk][j].first << " ";
					}
				}
			}
			else{ //col
				for (int j=0; j<n; j++){
					if (j==n-1){
						fout << grid[j][sk].first << endl;
					}
					else{
						fout << grid[j][sk].first << " ";
					}
				}
			}
			//print grid
			/*for (int j=0; j<n; j++){
				for (int k=0; k<n; k++){
					fout << grid[j][k].first << " ";
				}
				fout << endl;
			}
			for (int j=0; j<n; j++){
				vector<int> tmp;
				for (int k=0; k<n; k++){
					tmp.push_back(grid[j][k].first);
				}
				bool ans=true;
				for (int k=0; k<2*n-1; k++){
					if (tmp==v[k]){
						ans=false;
						break;
					}
				}
				if (ans){
					fout << "Defo Correct: ";
					for (int k=0; k<tmp.size(); k++){
						fout << tmp[k] << " ";
					}
					fout << endl;
				}
			}
			for (int j=0; j<n; j++){
				vector<int> tmp;
				for (int k=0; k<n; k++){
					tmp.push_back(grid[k][j].first);
				}
				bool ans=true;
				for (int k=0; k<2*n-1; k++){
					if (tmp==v[k]){
						ans=false;
						break;
					}
				}
				if (ans){
					fout << "Defo Correct: ";
					for (int k=0; k<tmp.size(); k++){
						fout << tmp[k] << " ";
					}
					fout << endl;
				}
			}*/
		}
		rows.clear();
		cols.clear();
		sk=-1;
	}
	fin.close();
	fout.close();
}
