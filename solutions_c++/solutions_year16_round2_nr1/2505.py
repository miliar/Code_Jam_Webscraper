#include<iostream>
#include<cstring>
#include<set>
#include<vector>
#include<iomanip>

using namespace std;



string s;
//int a[2005];


int main(){
	
	int i;
	int j=1;
	int t;
	cin>>t;
	while(t--){
	cin>>s;
	int n_=s.size();
	//cout<<s<<endl;
	int b[15];
	int z,o,w,r,u,f,x,v,g,n;
	z=o=w=r=u=f=x=v=g=n=0;
	for(i=0;i<n_;i++){
		if(s[i]=='Z'){
			z++;
		}
		if(s[i]=='O'){
			o++;
		}
		if(s[i]=='W'){
			w++;
		}
		if(s[i]=='R'){
			r++;
		}
		if(s[i]=='U'){
			u++;
		}
		if(s[i]=='F'){
			f++;
		}
		if(s[i]=='X'){
			x++;
		}
		if(s[i]=='V'){
			v++;
		}
		if(s[i]=='N'){
			n++;
		}
		if(s[i]=='G'){
			g++;
		}
	}
	//cout<<s[0]<<" "<<z<<" "<<o<<" "<<w<<" "<<r<<" "<<u<<" "<<f<<" "<<x<<" "<<v<<" "<<g<<" "<<n<<" "<<endl;
	b[0]=z;
	b[2]=w;
	b[4]=u;
	b[6]=x;
	b[8]=g;
	o-=z+u+w;
	b[1]=o;
	r-=u;
	r-=z;
	b[3]=r;
	f-=u;
	b[5]=f;
	v-=f;
	b[7]=v;
	n-=o;
	n-=v;
	n/=2;
	b[9]=n;
	cout<<"Case #"<<(j)<<": ";
	j++;
	for(i=0;i<=9;i++){
		int k;
		for(k=0;k<b[i];k++){
			cout<<i;
		}
			//cout<<b[i]<<" ";
	}cout<<endl;
	

	
	}

	return 0;
}