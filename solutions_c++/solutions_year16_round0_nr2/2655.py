#include <bits/stdc++.h>

using namespace std;
string cad,aux;
void reduce(){
    aux="";
    int l=cad.length();
    for (int i=1; i<l; i++){
        if (cad[i]!=cad[i-1]){
            aux+=cad[i-1];
        }
    }
    cad=aux;
    cad+='*';
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large_output.out","w",stdout);
    int t,cont;
    scanf("%d",&t);
    for (int _case=1; _case<=t; _case++){
        cin>>cad;
        cad+='*';
        reduce();
        cont=0;
        if (cad.length()==2 && cad[0]=='-') cont=1;
        while (cad.length()>2){
            if (cad[0]=='-' && cad[1]=='+'){
                cont++;
            }else if (cad[0]=='+' && cad[1]=='-'){
                cont+=2;
            }
            cad[0]='+';cad[1]='+';
            reduce();
        }
        printf("Case #%d: %d\n",_case,cont);
    }
    //fclose(stdin);
    //fclose(stdout);
    return 0;
}
