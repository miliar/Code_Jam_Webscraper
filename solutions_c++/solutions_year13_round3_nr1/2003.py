#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>

#define _for(i,n) for(long long i = 0; i<n; i++)
#define _fora(i,n) for(long long i = 1; i<=n; i++)
#define _forlor(i,n) for(long long i=n-1; i>=0; i--)
#define max(a,b) a<b?b:a
#define min(a,b) a>b?b:a

bool isvoy(char c){
	return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}
bool isntvoy(char c){
	return !(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

using namespace std;

int main(){
	freopen("in.in", "r", stdin);
	freopen("out.in", "w", stdout);


	int T;
	cin>>T;
	_fora(t,T){
		string s;
		int n;
		cin>>s;
		cin>>n;
		string::iterator bibi = s.begin();
		string::iterator lifat = bibi;
		int cmpt = 0;
		while(true){
			string::iterator firstntvoy = find_if(bibi,s.end(),isntvoy);
			if(firstntvoy == s.end())
				break;
			string::iterator firstvoy = find_if(firstntvoy,s.end(),isvoy);

			int taille = firstvoy - firstntvoy;
			
			//////////////////////////////////////////////////////////
			
			if (taille>=n)
			{
				//int chhalkbel = firstntvoy - s.begin();
				int nbrsubnonvoy = taille-n+1;
				_for(i,nbrsubnonvoy){//pour chaque subst
					
					int a = (1+(firstntvoy+i - lifat));
					int b = (s.end() - (firstntvoy+n+i) +1);
					cmpt+= a * b;

					lifat = firstntvoy+i+1;
				}
			}

			//////////////////////////////////////////////////////////

			bibi = firstvoy;
		}
		cout<<"Case #"<<t<<": "<<cmpt<<endl;;
	}

	return 0;
}
