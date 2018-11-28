#include <iostream>
#include <fstream>
#include <vector>
#include<iomanip>

using namespace std;

int main()
{
	ifstream arch;
	ofstream arch2;
	arch.open("B-large.in");
	arch2.open("res2.txt");

	int n;
	long double c,f,x,ans;
	long double r;
	long double dinero;
	arch >> n;

	for(int s=0; s<n; s++){
        ans=0.0;
        dinero=0.0;
        r=2.0;
        arch>>c>>f>>x;
        while(dinero!=x){
            if(dinero<c){
                /*double ans2=ans+(c-dinero)/r;
                dinero;
                if( ((ans2+(x-dinero+c)/(r+f))<(ans+(x-dinero)/(r))) ){
                    ans=ans2;
                    r+=f;
                    dinero-=c;
                } else {
                    dinero+=
                }*/
                double tiempoSig=(c-dinero)/r;
                double tiempoHastaFinal=(x)/(r+f);
                if( ans+(x-dinero)/r < ans+tiempoSig+tiempoHastaFinal ){

                    ans+=((x-dinero)/r);
                    dinero=x;
                    //cout << ans << endl;
                } else {
                    ans+=(c-dinero)/r;
                    dinero=0;
                    r+=f;
                }

            } else {
                dinero-=c;
                r+=f;
                if( (ans+(x-dinero)/r)<(ans+(x-dinero+c)/(r-f)) ){
                    //dinero+=c;
                    //r-=f;
                    ans+=(dinero-c)/r;

                } else {
                    ans+=(x-dinero+c)/(r-f);
                    dinero=x;

                }
            }
        }
        arch2 << "Case #" << s+1 << ": "  << setprecision(7) << fixed << ans << endl;
	}

	arch.close();
	arch2.close();

	return 0;
}


