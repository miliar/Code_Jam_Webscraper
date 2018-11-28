#include <bits/stdc++.h>

using namespace std;
#define LL long long
#define FORI(A,B,C) for(int I=(A);I<=(B); I++)
#define FORLL(A,B,C) for(L I=(A);I<=(B); I++)

LL fun(LL A, LL B, LL C){
	return -1;
}

	bool helper_RU(vector<int> &flag,vector<vector<LL>> &map,int N, int r,int c,vector<vector<LL>> &nums, int idx){
		if (r>N || c>N) return false;
		if (idx==2*N-1) return true;
		int canberow=0,canbecol=0;
		int rowidx=0,colidx=0;
		for (int i=0;i<N;i++){
			if (map[i][0]==nums[idx][0]){
				int j;
				for (j=1;j<N;j++){
					if (map[i][j]!=INT_MIN && map[i][j]!=nums[idx][j]) {
						canberow=0;
						break;
					}
				}
				if (j==N) canberow = 1;
				rowidx = i;
				break;
			}
		}
		for (int i=0;i<N;i++){
			if (map[0][i]==nums[idx][0]){
				int j;
				for (j=1;j<N;j++){
					if (map[j][i]!=INT_MIN && map[j][i]!=nums[idx][j]) {
						canbecol=0;
						break;
					}
				}
				if (j==N) canbecol = 1;
				colidx=i;
				break;
			}
		}
//		   for (auto &x:map){
//			   for (auto &y:x) {cout<<y<<" ";}
//			   cout<<endl;
//		   }
//		cout<<"idx"<<idx<<" "<<canberow<<" "<<canbecol<<endl;
//		 for (auto&x:flag) cout<<x<<" ";
//		 cout<<endl;
		if (canberow && flag[rowidx]==0) {
			flag[rowidx]=2;
			vector<vector<LL>> newmap = map;
			for (int i=0;i<N;i++){
				newmap[rowidx][i] = nums[idx][i];
			}
			if (helper_RU(flag,newmap,N,r+1,c,nums,idx+1)){
				map = newmap;
				flag[rowidx] = 1;
				return true;
			}
			flag[rowidx]=0;
		}
		if (canbecol && flag[colidx+N]==0) {
			flag[colidx+N]=2;
			vector<vector<LL>> newmap = map;
			for (int i=0;i<N;i++){
				newmap[i][colidx] = nums[idx][i];
			}
			if (helper_RU(flag,newmap,N,r,c+1,nums,idx+1)){
				map = newmap;
				flag[colidx+N] = 1;
				return true;
			}
			flag[colidx+N]=0;
		}
		return false;
	}

bool helper_RD(vector<int> &flag, vector<vector<LL>> &map,int N, int r,int c,vector<vector<LL>> &nums, int idx){
	if (r>N || c>N) return false;
	if (idx==2*N-1) return true;
	int canberow=0,canbecol=0;
	int rowidx=0,colidx=0;
	for (int i=0;i<N;i++){
		if (map[i][N-1]==nums[idx][N-1]){
			int j;
			for (j=0;j<N-1;j++){
				if (map[i][j]!=INT_MIN && map[i][j]!=nums[idx][j]) {
					canberow=0;
					break;
				}
			}
			if (j==N-1) canberow = 1;
			rowidx = i;
			break;
		}
	}
	for (int i=0;i<N;i++){
		if (map[N-1][i]==nums[idx][N-1]){
			int j;
			for (j=0;j<N-1;j++){
				if (map[j][i]!=INT_MIN && map[j][i]!=nums[idx][j]) {
					canbecol=0;
					break;
				}
			}
			if (j==N-1) canbecol = 1;
			colidx=i;
			break;
		}
	}
//	   for (auto &x:map){
//		   for (auto &y:x) {cout<<y<<" ";}
//		   cout<<endl;
//	   }
//	cout<<"idx"<<idx<<" "<<canberow<<" "<<canbecol<<endl;
//	 for (auto&x:flag) cout<<x<<" ";
//	 cout<<endl;
	if (canberow && flag[rowidx]==0) {
		flag[rowidx]=2;
		vector<vector<LL>> newmap = map;
		for (int i=0;i<N;i++){
			newmap[rowidx][i] = nums[idx][i];
		}
		if (helper_RD(flag,newmap,N,r+1,c,nums,idx+1)){
			map = newmap;
			flag[rowidx] = 1;
			return true;
		}
		flag[rowidx]=0;
	}
	if (canbecol && flag[colidx+N]==0) {
		flag[colidx+N]=2;
		vector<vector<LL>> newmap = map;
		for (int i=0;i<N;i++){
			newmap[i][colidx] = nums[idx][i];
		}
		if (helper_RD(flag,newmap,N,r,c+1,nums,idx+1)){
			map = newmap;
			flag[colidx+N] = 1;
			return true;
		}
		flag[colidx+N]=0;
	}
	return false;
}

vector<LL> funv(vector<vector<LL>> nums){
	LL N = nums[0].size();
	vector<vector<LL>> map(N,vector<LL>(N,INT_MIN));
	LL minV=INT_MAX,maxV=INT_MIN;
	for (int i=0;i<2*N-1;i++){
		minV = min(minV,nums[i][0]);
		maxV = max(maxV,nums[i][N-1]);
	}
	int cnt = 0;
	for (int i=0;i<2*N-1;i++){
		if (nums[i][0]==minV) cnt++;
	}
	bool row=1;
	if (cnt==1) {
		for (int i=0;i<2*N-1;i++){
			if (nums[i][N-1]==maxV)
				if (row){
					map[N-1] = nums[i];
					row = 0;
				}else{
					for (int j=0;j<N;j++){
						map[j][N-1]=nums[i][j];
					}
				}
			}
		}
     else{
		for (int i=0;i<2*N-1;i++){
			if (nums[i][0]==minV)
				if (row){
					map[0] = nums[i];
					row = 0;
				}else{
					for (int j=0;j<N;j++){
						map[j][0]=nums[i][j];
					}
				}
			}
		}
//	   for (auto &x:map){
//		   for (auto &y:x) {cout<<y<<" ";}
//		   cout<<endl;
//	   }
	vector<int> flag(2*N,0);
	cout<<cnt<<endl;
   if (cnt==2){
	   helper_RU(flag,map,N,0,0,nums,0);
   }else{
	   helper_RD(flag,map,N,0,0,nums,0);
   }
 for (auto&x:flag) cout<<x<<" ";
 cout<<endl;
   for (auto &x:map){
	   for (auto &y:x) {cout<<y<<" ";}
	   cout<<endl;
   }

   vector<LL> res;
   for (int i=0;i<N*2;i++){
	   if (flag[i]!=1){
		   if (i<N) return map[i];
	        else{
		   for (int j=0;j<N;j++){
			   res.push_back(map[j][i-N]);
		   }
          return res;
	      }
	   }
   }

}

int main() {
    ifstream ifile;
    ofstream ofile;
    ifile.open("Input.txt");
    ofile.open("Output.txt");

    int CaseIdx,TotalCase;
    string line;
    getline(ifile,line);
    stringstream ss(line);
    ss>>TotalCase;

    for (CaseIdx = 1; CaseIdx<=TotalCase; CaseIdx++)
    {
//  begin of code
  //  1. prepare data for current test case
    	LL N;
    	vector<vector<LL>> nums;

		{
			getline(ifile,line);
			stringstream ss(line);
			ss>>N;
		}
		for (int i=0;i<2*N-1;i++)
		{
			getline(ifile,line);
			stringstream ss(line);
			vector<LL> tempN;
			for (int i=0;i<N;i++)
			{LL temp;ss>>temp;tempN.push_back(temp);}
			nums.push_back(tempN);
		}

  //  2. data_pre_processing if possible. (significantly reduced time/space complextity


  //  3. data_processing to get the result
		//int res = fun(A,B,C);
		vector<LL> res = funv(nums);

  //  4. Output results;
		string caseResult="";
		for (auto &x:res)
		caseResult += to_string(x)+" ";
		caseResult.erase(caseResult.size()-1);
cout<<endl<<endl;
    	cout<<"Case #"<<CaseIdx<<": "<<caseResult<<endl;
    	ofile<<"Case #"<<CaseIdx<<": "<<caseResult<<endl;

// end of code
    }


    ifile.close();
    ofile.close();
	return 0;
}

