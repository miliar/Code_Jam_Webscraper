#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main() {
    // freopen("Dijkstra.txt","r",stdin);
    freopen("Dijkstrainput.txt","r",stdin);
    freopen("Dijkstraoutput.txt","w",stdout);
    int T,L,X,K,i,j,temp,flagi,flagj,val;
    char c[3];
    scanf("%d",&T);
    for(K=1;K<=T;K++) {
        scanf("%d%d",&L,&X);
        char S[L+1];
        scanf("%s",S);
        temp=L*X;
        c[0]='+';
        c[1]=S[0];
        c[2]='\0';
        // printf("C=%s\n",c);
        flagi=flagj=0;
        for(i=1;i<temp;i++) {
            // printf("i: %d c: %s\n",i,c);
            // Look for i
            if(flagi==0) {
                if(i>=L) {
                val=i%L;
                } else {
                    val=i;
                }
                if(strcmp(c,"+i")==0) {
                    flagi=1;
                    c[1]=S[val];
                    // printf("i=%d val=%d Got i\n",i,val);
                    continue;
                }
                if(strcmp(c,"+j")==0) {
                    if(S[val]=='i') {
                        c[0]='-';
                        c[1]='k';
                    } else if(S[val]=='j'){
                        c[0]='-';
                        c[1]='1';
                    } else {
                        c[0]='+';
                        c[1]='i';
                    }
                    continue;
                }
                if(strcmp(c,"+k")==0) {
                    if(S[val]=='i') {
                        c[0]='+';
                        c[1]='j';
                    } else if(S[val]=='j'){
                        c[0]='-';
                        c[1]='i';
                    } else {
                        c[0]='-';
                        c[1]='1';
                    }
                    continue;
                }
                if(strcmp(c,"-j")==0) {
                    if(S[val]=='i') {
                        c[0]='+';
                        c[1]='k';
                    } else if(S[val]=='j'){
                        c[0]='+';
                        c[1]='1';
                    } else {
                        c[0]='-';
                        c[1]='i';
                    }
                    continue;
                }
                if(strcmp(c,"-k")==0) {
                    if(S[val]=='i') {
                        c[0]='-';
                        c[1]='j';
                    } else if(S[val]=='j'){
                        c[0]='+';
                        c[1]='i';
                    } else {
                        c[0]='+';
                        c[1]='1';
                    }
                    continue;
                }
                if(strcmp(c,"+1")==0) {
                    if(S[val]=='i') {
                        c[0]='+';
                        c[1]='i';
                    } else if(S[val]=='j'){
                        c[0]='+';
                        c[1]='j';
                    } else {
                        c[0]='+';
                        c[1]='k';
                    }
                    continue;
                }
                if(strcmp(c,"-1")==0) {
                    if(S[val]=='i') {
                        c[0]='-';
                        c[1]='i';
                    } else if(S[val]=='j'){
                        c[0]='-';
                        c[1]='j';
                    } else {
                        c[0]='-';
                        c[1]='k';
                    }
                    continue;
                }
                if(strcmp(c,"-i")==0) {
                    if(S[val]=='i') {
                        c[0]='+';
                        c[1]='1';
                    } else if(S[val]=='j'){
                        c[0]='-';
                        c[1]='k';
                    } else {
                        c[0]='+';
                        c[1]='j';
                    }
                    continue;
                }
                continue;
            }
            // Look for j
            if(flagj==0) {
                if(i>=L) {
                val=i%L;
                } else {
                    val=i;
                }
                if(strcmp(c,"+j")==0) {
                    flagj=1;
                    c[1]=S[val];
                    // printf("i=%d val=%d Got j\n",i,val);
                    continue;
                }
                if(strcmp(c,"+i")==0) {
                    if(S[val]=='i') {
                        c[0]='-';
                        c[1]='1';
                    } else if(S[val]=='j'){
                        c[0]='+';
                        c[1]='k';
                    } else {
                        c[0]='-';
                        c[1]='j';
                    }
                    continue;
                }
                if(strcmp(c,"+k")==0) {
                    if(S[val]=='i') {
                        c[0]='+';
                        c[1]='j';
                    } else if(S[val]=='j'){
                        c[0]='-';
                        c[1]='i';
                    } else {
                        c[0]='-';
                        c[1]='1';
                    }
                    continue;
                }
                if(strcmp(c,"-j")==0) {
                    if(S[val]=='i') {
                        c[0]='+';
                        c[1]='k';
                    } else if(S[val]=='j'){
                        c[0]='+';
                        c[1]='1';
                    } else {
                        c[0]='-';
                        c[1]='i';
                    }
                    continue;
                }
                if(strcmp(c,"-k")==0) {
                    if(S[val]=='i') {
                        c[0]='-';
                        c[1]='j';
                    } else if(S[val]=='j'){
                        c[0]='+';
                        c[1]='i';
                    } else {
                        c[0]='+';
                        c[1]='1';
                    }
                    continue;
                }
                if(strcmp(c,"+1")==0) {
                    if(S[val]=='i') {
                        c[0]='+';
                        c[1]='i';
                    } else if(S[val]=='j'){
                        c[0]='+';
                        c[1]='j';
                    } else {
                        c[0]='+';
                        c[1]='k';
                    }
                    continue;
                }
                if(strcmp(c,"-1")==0) {
                    if(S[val]=='i') {
                        c[0]='-';
                        c[1]='i';
                    } else if(S[val]=='j'){
                        c[0]='-';
                        c[1]='j';
                    } else {
                        c[0]='-';
                        c[1]='k';
                    }
                    continue;
                }
                if(strcmp(c,"-i")==0) {
                    if(S[val]=='i') {
                        c[0]='+';
                        c[1]='1';
                    } else if(S[val]=='j'){
                        c[0]='-';
                        c[1]='k';
                    } else {
                        c[0]='+';
                        c[1]='j';
                    }
                    continue;
                }
                continue;
            }
            // Look for k
            if(i>=L) {
                val=i%L;
            } else {
                val=i;
            }
            if(strcmp(c,"+j")==0) {
                if(S[val]=='i') {
                    c[0]='-';
                    c[1]='k';
                } else if(S[val]=='j'){
                    c[0]='-';
                    c[1]='1';
                } else {
                    c[0]='+';
                    c[1]='i';
                }
                continue;
            }
            if(strcmp(c,"+i")==0) {
                if(S[val]=='i') {
                    c[0]='-';
                    c[1]='1';
                } else if(S[val]=='j'){
                    c[0]='+';
                    c[1]='k';
                } else {
                    c[0]='-';
                    c[1]='j';
                }
                continue;
            }
            if(strcmp(c,"+k")==0) {
                if(S[val]=='i') {
                    c[0]='+';
                    c[1]='j';
                } else if(S[val]=='j'){
                    c[0]='-';
                    c[1]='i';
                } else {
                    c[0]='-';
                    c[1]='1';
                }
                continue;
            }
            if(strcmp(c,"-j")==0) {
                if(S[val]=='i') {
                    c[0]='+';
                    c[1]='k';
                } else if(S[val]=='j'){
                    c[0]='+';
                    c[1]='1';
                } else {
                    c[0]='-';
                    c[1]='i';
                }
                continue;
            }
            if(strcmp(c,"-k")==0) {
                if(S[val]=='i') {
                    c[0]='-';
                    c[1]='j';
                } else if(S[val]=='j'){
                    c[0]='+';
                    c[1]='i';
                } else {
                    c[0]='+';
                    c[1]='1';
                }
                continue;
            }
            if(strcmp(c,"+1")==0) {
                if(S[val]=='i') {
                    c[0]='+';
                    c[1]='i';
                } else if(S[val]=='j'){
                    c[0]='+';
                    c[1]='j';
                } else {
                    c[0]='+';
                    c[1]='k';
                }
                continue;
            }
            if(strcmp(c,"-1")==0) {
                if(S[val]=='i') {
                    c[0]='-';
                    c[1]='i';
                } else if(S[val]=='j'){
                    c[0]='-';
                    c[1]='j';
                } else {
                    c[0]='-';
                    c[1]='k';
                }
                continue;
            }
            if(strcmp(c,"-i")==0) {
                if(S[val]=='i') {
                    c[0]='+';
                    c[1]='1';
                } else if(S[val]=='j'){
                    c[0]='-';
                    c[1]='k';
                } else {
                    c[0]='+';
                    c[1]='j';
                }
                continue;
            }
        }
        if(flagi==1 && flagj==1 && (strcmp(c,"+k")==0)) {
            printf("Case #%d: YES\n",K);
        } else {
            printf("Case #%d: NO\n",K);
        }
    }
    return 0;
}
