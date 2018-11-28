#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;

long long p,q,g;
long long power10[] = {1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000,100000000000,1000000000000,10000000000000,100000000000000,1000000000000000,10000000000000000};
char s[80],s1[80];

long long gcd(long long a, long long b){
  if(a==0){
    return b;
  }
  long long r = b%a;
  return gcd(r,a);
}

int logr(long long a, long long b){
  if(2*a >= b){
    return 1;
  }
  else{
    return 1+logr(2*a, b);
  }
}

int main(){
  int t,ii,i,j,l;
  cin>>t;
  for(ii=1;ii<=t;ii++){
    cout<<"Case #"<<ii<<": ";
    cin>>s;
    l = strlen(s);
    for(i=0;s[i]!='/';i++){
      s1[i] = s[i];
    }
    s1[i] = '\0';
    p = atoi(s1);
    i++;
    for(j=0;i<l;i++,j++){
      s1[j] = s[i];
    }
    s1[j] = '\0';
    q = atoi(s1);
//     cin>>p>>q;
    g = gcd(min(p,q),max(p,q));
    p/=g; q/=g;
//     cout<<(q & -q)<<endl;
    if((q != (q&-q)) || (p>q)){
      cout<<"impossible\n"; continue; 
    }
    cout<<logr(p,q)<<"\n";
  }
  return 0;
}
