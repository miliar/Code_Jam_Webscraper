#include<stdio.h>
#include<stdlib.h>
#include<fstream>


using namespace std;

int semn1;
char unu;

void f(char doi){
	int semn2=1; char what;
	if(unu=='1'){
		if(doi=='1'){what='1'; }
		if(doi=='i'){what='i'; }
		if(doi=='j'){what='j'; }
		if(doi=='k'){what='k'; }
	}
	else if(unu=='i'){
		if(doi=='1'){what='i'; }
		if(doi=='i'){what='1'; semn2=-1; }
		if(doi=='j'){what='k'; }
		if(doi=='k'){what='j'; semn2=-1;}
	}
	else if(unu=='j'){
		if(doi=='1'){what='j'; }
		if(doi=='i'){what='k'; semn2=-1;}
		if(doi=='j'){what='1'; semn2=-1; }
		if(doi=='k'){what='i'; }
	}
	else if(unu=='k'){
		if(doi=='1'){what='k'; }
		if(doi=='i'){what='j'; }
		if(doi=='j'){what='i'; semn2=-1; }
		if(doi=='k'){what='1'; semn2=-1;}
	}
	if(semn1==semn2) semn1=1;
	else  semn1=-1;
	unu=what;	
}



int main(){
int t, l,x;
string s, find="ijk";
ifstream in; ofstream out;
in.open("C-small-attempt0.in"); out.open("test.out");
out.clear();
in>>t;
for(int i=1;i<=t;i++){
	in>>l>>x>>s;
	unu=s[0];
	semn1=1;
	int where=0;
	for(int j=1;j<l*x;j++){
		while(unu==find[where] && where<=1 && semn1==1){
			unu=s[j%l]; semn1=1; j++;
			where++;
		}
		if(j<l*x) f(s[j%l]);
	}
   if(where==2 && unu=='k' && semn1==1) out<<"Case #"<<i<<": YES"<<endl;
   else out<<"Case #"<<i<<": NO"<<endl;
}





in.close(); out.close();	
return 0;	
}
