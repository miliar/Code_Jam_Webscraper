#include<bits/stdc++.h>
using namespace std;

int T,tc;
string s;
int pjgkue, batas, langkah; 
int i,j;

void balik(int a){
	string tmp="";
	for (int x=a; x<=batas; x++) tmp[x]=s[batas-x];
	for (int x=a; x<=batas; x++)
		if (tmp[x]=='+') s[x]='-';
		else s[x]='+';
}


int main(){
	cin.sync_with_stdio(0); cin.tie(0); 
	
	cin>> T ; 
	for (tc=1; tc<=T; tc++){
		cin>> s ;	pjgkue=s.size();	langkah=0;	
		
		
		for (i=pjgkue-1; i>=0; i--) if (s[i]=='-') {batas=i; break;}
		if (i==0) if (s[0]=='+') batas=-1;
	
		
		while (batas>=-1 && s.find('-')!=-1){
			
			langkah++;
			
				if (s[0]=='+') {
					for (i=0; s[i]!='-'; i++) ;
					for (j=0; j<i; j++)
						s[j]='-';
					
				}
					else
				balik(0); 
			
			
			
			for (i=batas; i>=0; i--) if (s[i]=='-'){batas=i;  break;}
			if (i<=0) if (s[i]=='+') {batas=-1; break; }
							
		}
	
	
		cout<<"Case #"<<tc<<": "<<langkah<<endl;
	}
	
}
