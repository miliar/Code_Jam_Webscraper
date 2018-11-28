# include <cstdio>
# include <cstring>
# include <cmath>
# include <cstdlib>
# include <iostream>
# include <vector>
# include <algorithm>
# include <queue>
# include <set>
# include <map>

using namespace std;

int main(){
int T;
cin>>T;
for(int tc=1;tc<=T;tc++){
 int ans_1,ans_2,grid_1[4][4],grid_2[4][4];
 int i,j;
 vector<int>row_1,row_2;
 cin>>ans_1;
 for(i=0;i<4;i++) for(j=0;j<4;j++) cin>>grid_1[i][j]; 
 for(i=0;i<4;i++) row_1.push_back(grid_1[ans_1-1][i]);
 cin>>ans_2;
 for(i=0;i<4;i++) for(j=0;j<4;j++) cin>>grid_2[i][j];
 for(i=0;i<4;i++) row_2.push_back(grid_2[ans_2-1][i]);
 sort(row_1.begin(),row_1.end());
 sort(row_2.begin(),row_2.end());
 
  int count = 0;
  int result = 0;
  i = 0; j = 0;
  while(i < 4 && j < 4)
  {
    if(row_1[i] < row_2[j])
      i++;
    else if(row_2[j] < row_1[i])
      j++;
    else /* if arr1[i] == arr2[j] */
    {
      //printf(" %d ", arr2[j++]);
      count++;
      result = row_1[i];
      i++;
    }
  }
 cout<<"Case #"<<tc<<": ";
 if(count == 1) cout<<result;
 else if(count > 1) cout<<"Bad magician!";
 else cout<<"Volunteer cheated!";
 cout<<endl;
}
return 0;
}
