#include <fstream>
#include <iostream>

using namespace std;

#define forn(i,n) for(int i = 0;i<n;i++)

int main(){
    int t;
    
    ifstream in ("B-large.in.txt");
    ofstream out ("cookie_large.out.txt");
    
    in>>t;
    
    forn (casen, t){
        double c,f,x;
        in>>c>>f>>x;
        
        double rate = 2.0;
        double seconds = 0.0;
        
        bool found = false;
        while (!found){
            double next_farm = c/rate;
            double time_with_f = next_farm + x / (rate+f);
            double time_without_f = x / (rate);
            //cout<<seconds<<endl;
            //cout<<next_farm<<endl;
            //cout<<time_with_f<<endl;
            //cout<<time_without_f<<endl;
            
            //time_without_f - time_with_f < 0.0000001
            if (time_with_f > time_without_f ){ //time_with_f > time_without_f
                seconds += time_without_f;
                //cout<<"SEE\n";
                found = true;
            }
            else {
                rate += f;
                seconds += next_farm;
            }
            
            //cin.get();
        }
        
//        cout<<"segundos: "<<seconds<<endl;
        char salida[100];
        sprintf(salida, "Case #%d: %.7f\n", casen + 1, seconds);
        out<<salida;
        //out<<"Case #"<<casen<<": "<<seconds<<endl;
    }
}
