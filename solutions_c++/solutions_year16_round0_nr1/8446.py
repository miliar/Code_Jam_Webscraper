#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int aux,n,r,k;
    int unit;
    int testCases;
    cin>>testCases;

    for(int i=0; i<testCases; i++){
        bool digitSeen[10]={false, false, false, false, false, false, false, false, false, false};
        cin>>n;
        if(n!=0){
            for(int j=1; j<=100000000; j++){
            r=n*j;
            aux=r;
            k=j;
                        while(aux>0){
                            unit=aux%10;
                            switch(unit){
                                case 0: digitSeen[0]=true;
                                    break;
                                case 1: digitSeen[1]=true;
                                    break;
                                case 2: digitSeen[2]=true;
                                    break;
                                case 3: digitSeen[3]=true;
                                    break;
                                case 4: digitSeen[4]=true;
                                    break;
                                case 5: digitSeen[5]=true;
                                    break;
                                case 6: digitSeen[6]=true;
                                    break;
                                case 7: digitSeen[7]=true;
                                    break;
                                case 8: digitSeen[8]=true;
                                    break;
                                case 9: digitSeen[9]=true;
                                    break;
                            }
                            aux=aux/10;
                        }

                if((digitSeen[0]) && digitSeen[1] && digitSeen[2] && digitSeen[3] && digitSeen[4] && digitSeen[5] && digitSeen[6] && digitSeen[7] && digitSeen[8] && digitSeen[9])break;
            }
            cout<<"Case #"<<i+1<<": "<<n*k<<endl;
        }
        else{
            cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
        }
    }
    return 0;
}
