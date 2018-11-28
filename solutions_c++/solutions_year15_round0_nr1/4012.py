#include<iostream>

using namespace std;

int main()
{
        int T;
                cin>>T;
                        
                        for(int i = 0; i < T;  i++) {
                                        int Smax;
                                                        cin>>Smax;
                                                                        int numPeopleWithShyI;
                                                                                        int numPeopleRequired = 0;
                                                                                                        int numPeopleIn = 0;
                                                                                                                        char c;
                                                                                                                                        for(int j = 0; j <= Smax; j++) {
                                                                                                                                                                cin>>c;
                                                                                                                                                                                        numPeopleWithShyI = c-'0';
                                                                                                                                                                                                                if(numPeopleIn < j && numPeopleWithShyI > 0) {
                                                                                                                                                                                                                                                numPeopleRequired += j - numPeopleIn;
                                                                                                                                                                                                                                                                                numPeopleIn += j - numPeopleIn;
                                                                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                        numPeopleIn += numPeopleWithShyI;
                                                                                                                                                                                                                                                        }
                                                                                                                                                        cout<<"Case #"<<i+1<<": "<<numPeopleRequired;
                                                                                                                                                                        if(i!= T-1)
                                                                                                                                                                                                cout<<endl;
                                                                                                                                                                                }
                                
                                return 0;
}
