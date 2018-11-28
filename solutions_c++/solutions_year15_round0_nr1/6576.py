#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n,i,number,j,n2,qt=0,person=0;
    char value;
    cin >> n;
    for(i=0;i<n;i++){
        qt=0;
        person=0;
        cin >> number;
        for(j=0;j<=number;j++){
            cin >> value;
            n2=value-48;
            if(n2>0 && person<j){
                qt+=(j-person);
                person+=(j-person);
            }
            person+=n2;
        }
        cout << "Case #" << i+1 << ": " << qt << endl;
    }
    return 0;
}
