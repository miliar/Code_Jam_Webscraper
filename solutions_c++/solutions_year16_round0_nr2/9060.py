#include<fstream>
#include<cstring>
using namespace std;
ifstream in("rev.in");
ofstream out("rev.out");
bool a[101];
int notdone(bool a[101], int p){
    for(int i=p;i>=0;i--)
        if(!a[i])
            return i;
    return -1;
}
void change(bool a[101], int p){
    for(int i=p;i>=0;i--)
        if(a[i])
            a[i]=false;
        else
            a[i]=true;
}
int main()
{
    int t,i,j,nr,po,newpo;
    char s[101];
    in>>t;
    in.get();
    for(i=1;i<=t;i++){
        in.getline(s,101);
        for(j=0;j<strlen(s);j++)
            if(s[j]=='+')
                a[j]=true;
            else
                a[j]=false;
        nr=0;
        po=strlen(s)-1;
        newpo=notdone(a,po);
        while(newpo>-1){
            change(a,newpo);
            nr++;
            newpo=notdone(a,newpo);
        }
        out<<"Case #"<<i<<": "<<nr<<"\n";
    }
    return 0;
}
