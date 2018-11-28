#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;


int map[4][4] = {1,2,3,4,
              2,-1,4,-3,
              3,-4,-1,2,
              4,3,-2,-1};

int value[10001][10001];

int get(char a){
    if(a=='i')
        return 2;
    else if(a=='j')
        return 3;
    else if(a=='k')
        return 4;
    return 0;
}

void substr(char str[],char string[],int i,int j){
    str[0] = '\0';
    strncpy(str,string+i,j-i);
    str[j-i] = '\0';
}

int evaluate(int s,char t){
    int ans=0,a=0;
    int flag = 0;
    int b = get(t);
    if(s<0){s = -s;flag = 1;}
    ans = map[s-1][b-1];
    if(flag){ans = -ans;}
    
    return ans;
}

void calc(char string[],int n){
    
    for(int i=0;i<=n;i++)
        value[i][i+1] = get(string[i]);
    
    for(int i=0;i<=n;i++){
        for(int j=i+2;j<=n;j++){
            value[i][j] = evaluate(value[i][j-1],string[j-1]);
        }
    }
}
int main(int argc, char *argv[]){
    int n;
    char a[4];
    ifstream fin(argv[1]);
    ofstream fout("output.txt");
    fin.getline(a,4);
    n = atoi(a);
    for(int test = 1;test<=n;test++){
        int l,x;
        int flag = 0;
        char lx[15],*p;
        fin.getline(lx,10005);
        p = strtok(lx," ");
        l = atoi(p);
        p = strtok(NULL," ");
        x = atoi(p);
        char  str[l+3],string[l*x+3];
        string[0] = '\0';
        fin.getline(str,10005);
        for(int i=0;i<x;i++){
            strcat(string,str);
        }
        calc(string,l*x);
        fout<<"Case #"<<test<<": ";
        for(int i=1;i<l*x-1;i++){
            int val1 = 100*value[0][i];
            for(int j=i+1;j<l*x;j++){
                int val = val1+10*value[i][j]+value[j][l*x];
                if(val == 234){flag = 1; fout<<"YES"<<endl;break;}
            }
            if(flag) break;
        }
        if(flag == 0) fout<<"NO"<<endl;
    }
    return 0;
}