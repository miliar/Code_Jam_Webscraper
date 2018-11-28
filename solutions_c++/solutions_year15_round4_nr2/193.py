#include<iostream>
#include<cmath>
#include<algorithm>
#include<complex>
#include<numeric>
#include<limits>

using namespace std;

typedef __float128 F;
typedef complex<F> P;

F fabs(F f){
  return f>0?f:-f;
}

ostream &operator<<(ostream &ost,__float128 f){
  return ost<<(long double)(f);
}

F eq(F a,F b){
  return fabs(a-b)<1e-8;
}

F cross(P a,P b){
  return a.real()*b.imag()-a.imag()*b.real();
}

int main(){
  int T;
  cin>>T;
  for(int c=1;c<=T;c++){
    int N;
    double V,X;
    cin>>N>>V>>X;
    double R[100],C[100];
    for(int i=0;i<N;i++){
      cin>>R[i]>>C[i];
    }
    double ans=-1;
    if(N==1){
      if(eq(C[0],X)){
	ans=V/R[0];
      }else{
	ans=-1;
      }
    }else{
      bool f=false;
      for(int i=0;i<N;i++){
	f|=!eq(C[i],X);
      }
      if(!f){
	ans=V/accumulate(R,R+N,0.);
      }else{
	int idx[100];
	iota(idx,idx+N,0);
	sort(idx,idx+N,[&](int a,int b){
	    return C[a]>C[b];
	  });
	const P dst(V,V*X);
	const auto m=10000/0.0001*2;
	F l=0,h=m;
	for(int i=0;i<100;i++){
	  auto m=(l+h)/2;
	  vector<P> v;
	  v.emplace_back(0,0);
	  for(int j=0;j<N;j++){
	    auto x=m*R[idx[j]];
	    v.push_back(v.back()+P(x,C[idx[j]]*x));
	  }
	  for(int j=0;j<N-1;j++){
	    auto x=-m*R[idx[j]];
	    v.push_back(v.back()+P(x,C[idx[j]]*x));
	  }
	  // cout<<dst.real()<<' '<<dst.imag()<<endl;
	  // for(auto e:v){
	  //   cout<<e.real()<<' '<<e.imag()<<endl;
	  // }
	  bool n=false,p=false;
	  for(int i=0;i<v.size();i++){
	    bool skip=false;
	    if(i==0||i==v.size()-1){
	      auto p=v[i==0?1:i];
	      //	      cout<<dst.imag()/dst.real()-p.imag()/p.real()<<endl;
	      if(fabs(dst.imag()/dst.real()-p.imag()/p.real())<1e-8&&dst.real()<p.real()){
		skip=true;
	      }
	    }
	    if(!skip){
	      auto c=cross(v[(i+1)%v.size()]-v[i],dst-v[i]);
	      ((c<0)?n:p)=true;
	      //	      cout<<c<<endl;
	    }
	    //	    cout<<n<<' '<<p<<endl;
	  }
	  if(n^p){
	    h=m;
	  }else{
	    l=m;
	  }	      
	}
	if(l>m/2){
	  ans=-1;
	}else{
	  ans=h;
	}
      }
    }
    cout<<"Case #"<<c<<": ";
    if(ans<0){
      cout<<"IMPOSSIBLE"<<endl;
    }else{
      cout.precision(9);
      cout<<fixed<<ans<<endl;
    }
  }
}
