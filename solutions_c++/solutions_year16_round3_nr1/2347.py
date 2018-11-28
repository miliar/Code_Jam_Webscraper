#include<iostream>
#include<queue>
using namespace std;
struct sajal{
char c;long long n;
};
struct compare
{
  bool operator()(sajal& l, sajal& r)
  {
      return l.n < r.n;
  }
};
char c[]={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
int main(){
int t;
cin>>t;
for(int i=0;i<t;i++){long n;
    cin>>n;long long int s=0;long a[n];
     priority_queue<sajal,vector<sajal>, compare > pq;
    for(long j=0;j<n;j++){cin>>a[j];s=s+a[j];
    sajal r;r.c=c[j];r.n=a[j];
    pq.push(r);}
    cout<<"Case #"<<i+1<<": ";n=s;
    while(!pq.empty()){
        sajal w=pq.top();
        pq.pop();
     //   cout<<w.n<<" djgjlg ewkfl "<<w.c<<" "<<n<<endl;
        n=n-1;cout<<w.c;
        w.n=w.n-1;
        if(w.n>0)pq.push(w);
        sajal r=pq.top();
        pq.pop();
        //  cout<<r.n<<" djgjlg ewkfl "<<r.c<<" "<<n<<endl;
        n=n-1;int x=0;sajal v;v.c='a';v.n=1;
        if(!pq.empty()) v=pq.top();
        else x=1;double e=1;
        if(x==0) e=v.n/(double)n;e=e*100;

        if(x==0&&e>50){n=n+1;pq.push(r);}
        else{r.n=r.n-1;cout<<r.c;if(r.n>0)pq.push(r);}
        cout<<" ";
    }
    cout<<endl;





}


}
