 #include <bits/stdc++.h>
using namespace std; 

#define MAX 220 
#define input freopen("in.txt","r",stdin)
#define output freopen("out.txt","w",stdout)
int main(){       
	//input;
	//output;
	long long x,y,n;
	cin >> n;
	for(int j=1;j<=n;j++){
		cin >> y;
		if(y==0)
			cout << "Case #"<<j<<": INSOMNIA"<<endl;
		else{
		long long i=1;
		string cad;
		while(true){
			x=y*i;
			i++;
			stringstream ss;
			ss << x;
			cad += ss.str();
			sort(cad.begin(),cad.end());
			char c= cad[0];
			string newcad,a;
			stringstream s1;
			s1 << c;
			s1 >> newcad;
			for(int k=1;k<cad.size();k++){
				if(c!=cad[k])
				{
					stringstream s1;
					c=cad[k];
					s1 << c;
					s1 >> a;
					newcad += a;
				}
			}
			cad=newcad;
			if(newcad.size()==10) 
				break;
		}
		cout <<"Case #"<<j<<": "<<x<<endl;
		}
	}
}
