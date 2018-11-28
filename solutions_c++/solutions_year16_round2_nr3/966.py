#include<bits/stdc++.h>
using namespace std;
pair<string,string>topics[20];
set<string>set1,set2;
set<string>::iterator its;

int main()
{
      int T,N,it,i,j,mask;
      freopen("C-small-attempt0.in","r",stdin);
      freopen("02.out","w",stdout);
      scanf("%d",&T);
      for(it=1; it<=T; it++)
      {
            scanf("%d",&N);
            for(i=0; i<N; i++){
                cin>>topics[i].first>>topics[i].second;
                //cout<<topics[i].first<<topics[i].second<<endl;
            }

            int ans=0;

            for(mask=1; mask<(1<<N); mask++)
            {
                  set1.clear();set2.clear();

                  for(j=0; j<N; j++){
                       if( (mask&(1<<j)) != 0 ){
                          //   if(mask==3)  cout<<"first:"<<topics[j].first<<endl;
                          //   if(mask==3)  cout<<"second:"<<topics[j].second<<endl;
                             set1.insert(topics[j].first);
                             set2.insert(topics[j].second);
                       }
                  }


                  int popcnt = 0;
                  int flag=1;
                  for(j=0; j<N; j++){
                       if( (mask&(1<<j)) == 0 ){
                            popcnt++;
                            if(set1.find(topics[j].first)==set1.end() || set2.find(topics[j].second)==set2.end()){
                                flag=0;
                                break;
                            }
                       }
                  }

                  if(flag){
                       ans = max(ans,popcnt);
                  }
            }

            printf("Case #%d: %d\n",it,ans);
      }
      return 0;
}
