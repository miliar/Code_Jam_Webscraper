
#include <iostream>
#include <stdio.h>
#include <fstream>

using namespace std;

ofstream outfile;
long double fCost = 0.0;
long double fProfit = 0.0;
long double targetCookies = 0.0;
long double cps = 2.0;
int curCase = 0;
int arraySize = 0;

void binarySearch(int arrSiz);
void findMinTime(long double cps,long double waitTime,long double PrevWaitTime);

int main(int argc, const char * argv[])
{
    
    outfile.open("/Users/vivekshivam/Desktop/Cookies.txt");
    
    char ch;
    fstream fin("/Users/vivekshivam/Desktop/input.in", fstream::in);
    char *ch1 = new char[3];
    int startIndex = 0;
    int count = 0;
    int testCase = 0;
    // for testcase
    while (fin >> noskipws >> ch) {
        if(ch == ' ' || ch == '\n'){
            ch1[startIndex] = '\0';
            testCase = atoi(ch1);
            cout <<"testCase "<< testCase;
            break;
            delete [] ch1;
        }
        else{
            ch1[startIndex] = ch;
            startIndex++;
        }
    }
    
    for(int i = 0; i < testCase; i++){
        curCase = i;
        // Cookies for the farm
        int startIndex = 0;
        count = 0;
        char *ch2 = new char[3];
        while (fin >> noskipws >> ch) {
            
            if(ch == ' ' || ch == '\n'){
                count++;
                ch2[startIndex] = '\0';
                long double val = atof(ch2);
                cout<<"\n val "<<val;
                if(count == 1){
                    fCost = val;
                }
                else if(count == 2){
                    fProfit = val;
                }
                else if(count == 3){
                    targetCookies = val;
                    findMinTime(2.0,(targetCookies / 2.0),0.0);
                    break;
                }
                startIndex = 0;
                delete [] ch2;
                ch2 = new char[3];
            }
            else{
                ch2[startIndex] = ch;
                startIndex++;
            }
        }
    }
    outfile.close();
    return 0;
}

void findMinTime(long double cps,long double prevWaitTime,long double waitTimeTobuy){
    
    long double nextWt = ((waitTimeTobuy + (fCost / cps)) + (targetCookies / (cps + fProfit)));
    if(nextWt < prevWaitTime) {
        waitTimeTobuy += (fCost / cps);
        findMinTime((cps + fProfit),nextWt, waitTimeTobuy);
    }
    else{
        cout<<"Case #"<<(curCase + 1)<<": "<< prevWaitTime;
        char *data = new char[100];
        sprintf(data, "Case #%d: %Lf",(curCase+1),prevWaitTime);
        outfile << data << endl;
        delete [] data;
        
        //found minimum time in int form then go for float form.
    }
}


















