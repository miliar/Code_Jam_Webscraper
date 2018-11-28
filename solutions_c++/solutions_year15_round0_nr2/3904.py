#include <iostream>
#include <cstdio>

using namespace::std;
int n, T, talerz[10000], answer, granica;

void brut(int licz, int tab[], int n){
if(licz>granica) return;
bool ok=false;
    for(int i=0; i<n; i++){
       //cout<<tab[i]<<" ";
        if(tab[i]>0) ok=true;
    }//cout<<"  licznik: "<<licz<<endl;
    if(!ok){
    answer=min(answer, licz);
    return;
    }

    for(int i=0; i<n; i++){
        tab[i]--;
    }

    brut(licz+1, tab, n);

    int id, maksi=0, mini=1000000009, id2;
    for(int i=0; i<n; i++){
        tab[i]++;
        //if(tab[i]<0) tab[i]=0;
        if(tab[i]>maksi) {maksi=tab[i]; id=i;}
        if(tab[i]<mini) {mini=tab[i]; id2=i;}
    }
    if(maksi>1){
            if((maksi+mini)%2==0 && id!=id2){
                tab[id]=(maksi+mini)/2;
                tab[id2]=(maksi+mini)/2;
                brut(licz+1, tab, n);
                tab[id]=maksi;
                tab[id2]=mini;
            }
            n++;
            for(int i=1; i<=maksi/2; i++){
                    tab[id]=maksi-i;
                    tab[n-1]=i;
                    brut(licz+1, tab, n);
                }
            tab[id]=maksi;
            tab[n-1]=0;
    }

}

int main() {
cin>>T;
for(int test=1; test<=T; test++){
cin>>n;
granica=0;
for(int i=0; i<n; i++){
    cin>>talerz[i];
    granica=max(granica, talerz[i]);
}
answer=1000000009;
brut(0, talerz, n);
printf("Case #%d: %d\n", test, answer) ;
for(int i=0; i<n; i++){
    talerz[i]=0;
}
}


return 0;
}
