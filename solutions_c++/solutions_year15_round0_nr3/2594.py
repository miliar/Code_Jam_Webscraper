//C
#include <iostream>
#include <map>
#include <string>
#include <cstdio>
using namespace std;
typedef pair<string,string> cc;
map<string,char> dp;
string s;
int m[5][5] = {{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
int v[10050];

int tro(int a, int r)
{
    int i;
    if(a<0)
    {
        a=-a;
        r=-r;
    }
    for(i=1;i<5;i++)
        if(m[a][i]==r){			
            return i;
		}
    return 1;
}

int conta(int a, int b)
{
    if(a<0)
    {
        if(b<0){
            return m[-a][-b];
		}
        else{
            return -m[-a][b];
		}
    }
    if(b<0){
        return -m[a][-b];
	}
    return m[a][b];
}

int tudo()
{
    int r = 1;
    int i;
    for(i=0;i<(int)s.size();i++)
    {
        r = conta(r, v[i]);
    }
    return r;
}

int main(){
	
	int t;
	cin>>t;
	int n = t;
	
	bool ok; 
	while(t--){
		int l,x;
		cin>>l>>x;		
		cin.ignore();
		string tr;
		cin>>tr;
		ok=false;
		//cout<<tr<<endl;
		s="";
		while(x--){
			s+=tr;
		}
		int p = 0;    
		for(int i=0;i<(int)(s.size());i++)
		{
			v[p++] = s[i]-'i'+2;
		}
		int p1,p2,p3;
    
		p = tudo();
		p1 = 1;
		for(int i=0;i<(int)(s.size())-2;i++)
		{
			p1 = conta(p1, v[i]);
			
			p2 = 1;
			if(p1==2)
			for(int j=i+1;j<(int)(s.size())-1;j++)
			{
				p2 = conta(p2, v[j]);
				if(p2==3)
				p3 = tro(conta(p1, p2), p);
				
				if(p1==2 && p2==3 && p3==4)
					ok =true;
			}
		}
		
		
		cout<<"Case #"<<n-t<<": "<<(ok?"YES":"NO")<<endl;
	}
	return 0;
}
