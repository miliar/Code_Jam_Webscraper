#include <bits/stdc++.h>
using namespace std;
typedef long long ll;


int main(int argc, const char * argv[]){
int TT;cin >> TT;
for(int ii=0;ii<TT;ii++){
int N;cin >> N;
int F[N];
for(int i=0;i<N;i++){cin >> F[i];F[i]--;}
int ans=0;


int L[N];memset(L,0,sizeof L);
bool mark[N];memset(mark,0,sizeof mark);
for(int i=0;i<N;i++){
  set<int> myset;
  myset.insert(i);
  int j=i;
  while(!myset.count(F[j])){
    if(j==F[F[j]]){
      //cerr<<"viewing "<<i<<" found:"<<j<<" and "<<F[j]<<" are pair buddies"<<F[F[i]]<<endl;
        L[j]=max(L[j],(int)myset.size()-1);
    }
    myset.insert(F[j]);
    j=F[j];
  }

  if(F[j]==i){
    //cycle, might be max answer
    ans=max(ans,(int)myset.size());
    if(myset.size()==2)
      mark[i]=true;
  }
}
/*
for(int i=0;i<N;i++)cerr << L[i]<< " ";
cerr<<endl;
for(int i=0;i<N;i++)cerr << mark[i]<< " ";
cerr<<endl;
*/
int tempans=0;
for(int i=0;i<N;i++){
  if(mark[i]){
    tempans+=L[i]+L[F[i]]+2;
    mark[F[i]]=0;
  }
}
ans=max(ans,tempans);
cout << "Case #"<<ii+1<<": "<<ans<<endl;
}
}
