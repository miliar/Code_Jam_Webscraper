#include<iostream>
#include<cstring>
#include<fstream>

using namespace std;

string flip(string,int);

int main(){
    ifstream fin;
    ofstream fout("out_large.txt");
    fin.open ("in_large.in");

    int case_no,s,count=0,x;
    string str,accept_str;
    fin>>case_no;
    s=case_no;
    while(s--){
    	count=0;
        fin>>str;
        accept_str=str;
        for(int i=0;i<accept_str.length();i++){
            if(accept_str[i]=='-')
            accept_str[i]='+';
        }
    //    cout<<accept_str<<endl;
        x=str.length();
        while(str!=accept_str){        
            while(str[x-1]=='+')
            	x=x-1;
            	
            str=flip(str,x--);
            
            count++;
        }
        fout<<"Case #"<<case_no-s<<": "<<count<<endl;
    }
    fin.close();
    fout.close();
}
//flip logic
string flip(string str,int x){
	int n;
//	cout<<x <<endl;
/*	for(int j=0;str[j]=='-';j++){
		n++;
		if(str[j]='+')
			break;
	}*/
    string str_c=str.substr(0,x);
    for(int i=0;i<x;i++){
        if(str_c[i]=='+')
            str_c[i]='-';
        else 
			str_c[i]='+';
    }
    str.replace(0,x,str_c);
    return str;
}
