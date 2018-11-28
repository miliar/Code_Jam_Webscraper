#include<fstream>
#include<map>
#include<iostream>
#include<cmath>

using namespace std;

map<long long,int> pnos;
long long ans=0;
int bits[16]={0};
int n,j;

inline void split(){
  long long a=0;
  for(int i=0;i<n;i++){
    a=1<<(n-i-1);
    if(a&ans)
      bits[i]=1;
    else
      bits[i]=0;
  }
}

inline long long n2(){
  long long no=0;
  for(int i=0;i<n;i++){
    if(bits[i]){
      no+=pow(2,n-i-1);
    }
  }
  return no;
}
inline long long n3(){
  long long no=0;
  for(int i=0;i<n;i++){
    if(bits[i]){
      no+=pow(3,n-i-1);
    }
  }
  return no;
}
inline long long n4(){
  long long no=0;
  for(int i=0;i<n;i++){
    if(bits[i]){
      no+=pow(4,n-i-1);
    }
  }
  return no;
}
inline long long n5(){
  long long no=0;
  for(int i=0;i<n;i++){
    if(bits[i]){
      no+=pow(5,n-i-1);
    }
  }
  return no;
}
inline long long n6(){
  long long no=0;
  for(int i=0;i<n;i++){
    if(bits[i]){
      no+=pow(6,n-i-1);
    }
  }
  return no;
}
inline long long n7(){
  long long no=0;
  for(int i=0;i<n;i++){
    if(bits[i]){
      no+=pow(7,n-i-1);
    }
  }
  return no;
}
inline long long n8(){
  long long no=0;
  for(int i=0;i<n;i++){
    if(bits[i]){
      no+=pow(8,n-i-1);
    }
  }
  return no;
}
inline long long n9(){
  long long no=0;
  for(int i=0;i<n;i++){
    if(bits[i]){
      no+=pow(9,n-i-1);
    }
  }
  return no;
}
inline long long n10(){
  long long no=0;
  for(int i=0;i<n;i++){
    if(bits[i]){
      no+=pow(10,n-i-1);
    }
  }
  return no;
}

int main(){
  ifstream primes;
  int no,temp,nsol=0;
  long long d2=0,d3=0,d4=0,d5=0,d6=0,d7=0,d8=0,d9=0,d10=0;
  primes.open("17.txt", std::ifstream::in);
  primes>>temp;
  pnos[temp]=1;
  while (primes.good()) {
    primes>>temp;
    pnos[temp]=1;
  }
  primes.close();
  scanf("%d",&temp);
  scanf("%d %d",&n,&j);
  ans=1<<(n-1);
  ans++;
  ans+=2;
  printf("Case #1:\n");
  while(nsol<j){
    split();
    d2=0;d3=0;d4=0;d5=0;d6=0;d7=0;d8=0;d9=0;d10=0;
    if((pnos[n2()]!=1&&pnos[n3()]!=1&&pnos[n4()]!=1&&pnos[n5()]!=1&&pnos[n6()]!=1&&pnos[n7()]!=1&&pnos[n8()]!=1&&pnos[n9()]!=1&&pnos[n10()]!=1)){
      for(map<long long,int>::iterator it=pnos.begin();; ++it){
        if(n2()%(it->first)==0){
          d2=(it->first);
          break;
        }
      }
      for(map<long long,int>::iterator it=pnos.begin();; ++it){
        if(n3()%(it->first)==0){
          d3=(it->first);
          break;
        }
      }
      for(map<long long,int>::iterator it=pnos.begin();; ++it){
        if(n4()%(it->first)==0){
          d4=(it->first);
          break;
        }
      }
      for(map<long long,int>::iterator it=pnos.begin();; ++it){
        if(n5()%(it->first)==0){
          d5=(it->first);
          break;
        }
      }
      for(map<long long,int>::iterator it=pnos.begin();; ++it){
        if(n6()%(it->first)==0){
          d6=(it->first);
          break;
        }
      }
      for(map<long long,int>::iterator it=pnos.begin();; ++it){
        if(n7()%(it->first)==0){
          d7=(it->first);
          break;
        }
      }
      for(map<long long,int>::iterator it=pnos.begin();; ++it){
        if(n8()%(it->first)==0){
          d8=(it->first);
          break;
        }
      }
      for(map<long long,int>::iterator it=pnos.begin();; ++it){
        if(n9()%(it->first)==0){
          d9=(it->first);
          break;
        }
      }
      for(map<long long,int>::iterator it=pnos.begin();; ++it){
        if(n10()%(it->first)==0){
          d10=(it->first);
          break;
        }
      }
      if((d2==n2())||(d3==n3())||(d4==n4())||(d5==n5())||(d6==n6())||(d7==n7())||(d8==n8())||(d9==n9())||(d10==n10()))
        goto label;
      for(int z=0;z<n;z++){
        cout<<bits[z];
      }
      cout<<" ";
       printf("%lld %lld %lld %lld %lld %lld %lld %lld %lld\n",d2,d3,d4,d5,d6,d7,d8,d9,d10);
       // printf("%lld %lld %lld %lld %lld %lld %lld %lld %lld\n",n2(),n3(),n4(),n5(),n6(),n7(),n8(),n9(),n10());
       nsol++;
    label:;
    }
    ans+=2;
  }
  return 0;
} 
