#include<simplecpp>
#include<fstream>

int pl(string ,int);
int mi(string a,int iter){
string k;
int i,j;
if(a.length()==1 && a[0]=='-')
    return iter;
if(a[a.length()-1]=='-')
    a=a.substr(0,a.length()-1);
if(a[0]=='+'){
    for(i=0;i<a.length();i++){
        if(a[i]=='+')
            k[i]='-';
        else
            k[i]='+';
        }
    for(i=0;i<a.length();i++){
        a[i]=k[a.length()-i-1];
        }
    return mi(a,iter+1);
    }
return pl(a,iter+1);

}

int pl(string a,int iter){
string k;
int i,j;
if(a.length()==1 && a[0]=='+')
    return iter;
if(a[a.length()-1]=='+')
    a=a.substr(0,a.length()-1);
if(a[0]=='-'){
    for(i=0;i<a.length();i++){
        if(a[i]=='+')
            k[i]='-';
        else
            k[i]='+';
        }
    for(i=0;i<a.length();i++){
        a[i]=k[a.length()-i-1];
        }
    return pl(a,iter+1);
    }
return mi(a,iter+1);
}

main_program{
ifstream infile("1.in");
ofstream outfile("2.in");
int i,j,ans,lines,lines1;
lines1=1;
infile>>lines;
while(lines--){
string k,r;
infile>>k;
r=k[0];
for(i=1;i<k.length();i++){
    if(k[i]!=k[i-1]){
        r=r+k[i];
        }
    }
ans=pl(r,0);
outfile<<"Case #"<<lines1<<": "<<ans<<endl;
lines1++;
}
}
