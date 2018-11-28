#include<iostream>
#include<cstdio>
#include<string>
#include<sstream>
using namespace std;
typedef unsigned long long uint64;

uint64 fromstring(string v){
	stringstream ss;
	uint64 t;	
	ss<<v;
	ss>>t;
	return t;
}
string tostring(uint64 v){
	stringstream ss;
	string s;	
	ss<<v;
	ss>>s;
	return s;
}
uint64 fairize(uint64 v){
	string s=tostring(v);
	int len=s.length();
	string s2="";
	s2.resize(len*2);
	for(int i=0;i<len;i++){
		s2[i]=s[len-1-i];
		s2[len+i]=s[i];
	}
	uint64 nv=fromstring(s2);
	return nv;
}
uint64 fairize(uint64 v, int digit){
	string s=tostring(v);
	int len=s.length();
	string s2="";
	s2.resize(len*2+1);
	for(int i=0;i<len;i++){
		s2[i]=s[len-1-i];
		s2[len+1+i]=s[i];
	}
	s2[len]=(char)(digit+48);
	uint64 nv=fromstring(s2);
	return nv;
}

inline bool test(string s){
	//cout<<"test: "<<s<<endl;
	int len=s.length();
	for(int i=0;i<len/2;i++){
		if(s[i]!=s[len-1-i])return false;
	}
	return true;
}
inline bool test(uint64 sv){
	string s=tostring(sv);
	return test(s);
}	
bool squaretest(uint64 v){
	uint64 sv=v*v;
	return test(sv);
}
template <typename type>
type isqrt (type remainder)
{
  if (remainder < 0) // if type is unsigned this will be ignored = no runtime
    return 0; // negative number ERROR

  type place = (type)1 << (sizeof (type) * 8 - 2); // calculated by precompiler = same runtime as: place = 0x40000000
  while (place > remainder)
    place /= 4; // optimized by complier as place >>= 2

  type root = 0;
  while (place)
  {
    if (remainder >= root+place)
    {
      remainder -= root+place;
      root += place * 2;
    }
    root /= 2;
    place /= 4;
  }
  return root;
}

int main(){
	freopen("C-small-attempt0.in","r",stdin);freopen("c.out","w",stdout);
	//freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	//freopen("C-large-practice.in","r",stdin);freopen("C-large-practice.out","w",stdout);
	int numIter;
	scanf("%d",&numIter);
	for(int t=0;t<numIter;t++){
		uint64 A,B;
		uint64 c=0;
		cin>>A>>B;
		uint64 sa=isqrt(A);
		uint64 sb=isqrt(B);
		string s=tostring(sa);
		int len=s.length();
		int hlen=len/2;
		uint64 pa=1;
		//for(int i=0;i<hlen;i++){
		//	pa*=10;
		//}
		s=tostring(sb);
		 len=s.length();
		 hlen=len/2+len%2;
		uint64 pb=1;
		for(int i=0;i<hlen;i++){
			pb*=10;
		}
		pb*=10;
		//printf("pa=%lld pb=%lld\n",pa,pb);
		for(uint64 i=0;i<9;i++){
				uint64 nvsq=i*i;
				//printf("nv=%lld nvsq=%lld\n",i,nvsq);
				if(nvsq<A||nvsq>B)continue;
				if(test(nvsq)){c++;}
		}
		for(uint64 i=pa;i<=pb;i++){
			uint64 nv;
			for(int j=0;j<=10;j++){
				if(j==10){
					nv=fairize(i);
				}else{	
					nv=fairize(i,j);
				}
				uint64 nvsq=nv*nv;
				//printf("nv=%lld nvsq=%lld\n",nv,nvsq);
				if(nvsq<A||nvsq>B)continue;
				if(test(nvsq)){c++;}
			}	
		}
		
		cout<<"Case #"<<t+1<<": "<<c<<endl;

	}
	return 0;
}
