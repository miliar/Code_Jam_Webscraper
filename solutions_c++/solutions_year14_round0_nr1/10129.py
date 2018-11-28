#include <bits/stdc++.h>

using namespace std;

int main()
{

    //freopen("","r",stdin);
    freopen("out.txt","w",stdout);

    int t,n,i,j,caseno = 0,k;
    int arr[10][20];

    cin>>t;

      while(t--){

          cin>>n;

          for(i=0 ;i<4;i++)
          for(j=0 ;j<4 ;j++){

              cin>>k;
              arr[i][j] = k;

          }

          vector<int>v1,v2,ans;

          for(i=0 ;i<4;i++){

              v1.push_back(arr[n-1][i]);
          }

          cin>>n;
          for(i=0 ;i<4;i++)
          for(j=0 ;j<4 ;j++){

              cin>>arr[i][j];

          }

          for(i=0 ;i<4;i++){

              v2.push_back(arr[n-1][i]);
          }


        for(i=0 ;i<4;i++)
          for(j=0 ;j<4 ;j++){

              if(v1[i]==v2[j]){

                 ans.push_back(v2[j]);
              }
          }

          if(ans.size()==1)
              printf("Case #%d: %d\n",++caseno,ans[0]);
          else if(ans.size()==0)
              printf("Case #%d: Volunteer cheated!\n",++caseno);
          else
              printf("Case #%d: Bad magician!\n",++caseno);

      }


    return 0;
}
