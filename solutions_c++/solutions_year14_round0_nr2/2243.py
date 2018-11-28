#include<fstream>

using namespace std;

int main() {
    double c,f,x,cookie_rate=2,tempans,output;
    int T;
    ofstream writeoutput;
    ifstream readinput;
    writeoutput.open("Output_b_large.txt",ios::out);
    readinput.open("B-large.in",ios::in);
    readinput>>T;
    readinput.precision(10);
    writeoutput.precision(10);
    for(short i=1;i<=T;i++) {
        output=0;
        tempans=0;
        cookie_rate=2;
        readinput>>c;
        readinput>>f;
        readinput>>x;
       
        if(c/cookie_rate>=x/cookie_rate) {
            output=x/cookie_rate;
            writeoutput<<"Case #"<<i<<": "<<output<<endl;
        }
        else {
            while(1) {
                tempans=tempans+c/cookie_rate;
                cookie_rate= cookie_rate+f;
                if((tempans+(x/cookie_rate))>=(output+(x/(cookie_rate-f)))) {
                    output=output+x/(cookie_rate-f);
                    writeoutput<<"Case #"<<i<<": "<<output<<endl;
                    break;
                }
                else {
                    output=output+(tempans-output);
                }
            }
        }
    }
    readinput.close();
    writeoutput.close();
    return 0;
}
