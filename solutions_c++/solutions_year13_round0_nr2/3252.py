#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

string filename("ProblemB_Data_Big.txt");
int maxA = 100;

void rmRow(vector<vector<int> > & lawn,vector<int> & cnt,int & M, int & N,int irow);
void rmCol(vector<vector<int> > & lawn,vector<int> & cnt,int & M, int & N,int icol);
void print_mat(const vector<vector<int> > & mat);

int main()
{
	ifstream infile(filename.c_str());
	if (infile)
    {
		ofstream outfile((string("Output_")+filename).c_str());
		if (outfile)
		{
			// read the input file
			int T;
			infile>>T;
			for (int icase = 1; icase <= T; icase++)
			{
				int N,M,irow,icol,failflag = 0;
				infile>>N>>M;
				vector<int> temp(M,0), cnt(maxA,0);
				vector<vector<int> > lawn;
				for (int iN = 1; iN <= N; iN++){
					for (int iM = 1; iM<= M; iM++){
						infile>>temp[iM-1];
						cnt[temp[iM-1]-1]++;
					}
					lawn.push_back(temp);
				}
				//print_mat(lawn);
				
				for (int icnt = 1; icnt<=maxA; icnt++){
					if (cnt[icnt-1] == 0){continue;}
					while(cnt[icnt-1]>0 && M>0 && N>0){
						irow = 0;
						while(irow<N){
							vector<int>::iterator pos = find(lawn[irow].begin(), lawn[irow].end(), icnt);
							if (pos != lawn[irow].end()){
								icol = distance(lawn[irow].begin(), pos);
								break;
							}else{irow++;} 
							
						}
						if (lawn[irow] == vector<int>(M,icnt)){
							rmRow(lawn,cnt,M,N,irow);
							//print_mat(lawn);
						}else{
							
							for (int j = 0; j<N;j++){
								if (lawn[j][icol] != icnt){
									failflag = 1;
									break;
								}
							}
							if (failflag == 0) {
								rmCol(lawn,cnt,M,N,icol);
							//	print_mat(lawn);
							}else{break;}
						}
					}
					if (failflag == 1) {break;}
				}
				if (failflag == 1){
					outfile<<"Case #"<<icase<<": NO\n";
				}else{
					outfile<<"Case #"<<icase<<": YES\n";
					}		
			}
			
		}else{cout<<"Cannot create output file.\n"; return -1;}
    }else{cout<<"Cannot read the input file.\n"; return -1;}
	return 0;
}

void rmRow(vector<vector<int> > & lawn,vector<int> & cnt,int & M, int &N,int irow){
	N = N-1;
	for (int i = 0; i<M; i++){
		cnt[lawn[irow][i]-1]--;
	}
	lawn.erase(lawn.begin()+irow, lawn.begin()+irow+1);
}
void rmCol(vector<vector<int> > & lawn,vector<int> & cnt,int & M, int &N,int icol){
	M--;
	for (int j = 0; j<N; j++){
		cnt[lawn[j][icol]-1]--;
		lawn[j].erase(lawn[j].begin()+icol, lawn[j].begin()+icol+1);
	}
}
void print_mat(const vector<vector<int> > & mat){
	int N = mat.size();
	cout<<endl;
	for (int iN = 0; iN<N;iN++){
		for (vector<int>::const_iterator pos = mat[iN].begin(); pos!=mat[iN].end(); pos++){
			cout<<*pos<<" ";
		}
		cout<<endl;
	}
	cout<<endl;
}