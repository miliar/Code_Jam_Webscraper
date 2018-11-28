#include <bits/stdc++.h>
using namespace std;
int main()
{
    int casos, caso=1;
    cin>>casos;
    while(casos--)
    {
    int x,r,c, fact;
    bool ric=false;
    string queso;
    cin>>x>>r>>c;/*
    if(r>c){
    int aux=r;
    r=c;
    c=aux;
    }*/
    fact=r*c;
    switch(x)
    {
    case 1:
        queso="GABRIEL";
        break;
    case 2:
        if(fact==1 || fact==3 || fact==9)
            queso="RICHARD";
        else
            queso="GABRIEL";
        break;
    case 3:
        if(fact==6 || fact==9 || fact==12)
            queso="GABRIEL";
        else
            queso="RICHARD";
        break;
    case 4:
        if(fact<=9)
            queso="RICHARD";
        else
            queso="GABRIEL";
        break;
    }

        printf("Case #%d: ",caso);
        cout<<queso<<endl;
        caso++;
    }




    return 0;
}
