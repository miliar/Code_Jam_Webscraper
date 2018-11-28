#include <iostream>
#include <string>
using std::cin;
using std::cout;
using std::endl;

int main(void)
{
    int cases;
    cin >> cases;
    for(int i=1 ; i<=cases ; ++i){
        cout << "Case #" << i << ": ";

        int maxShyness;
        std::string input;
        cin >> maxShyness >> input;
        int friendsNeeded(0), audienceStood( input[0] - '0' );

        for(int j=1 ; j<=maxShyness ; ++j){
            if( audienceStood < j ){
                friendsNeeded += j - audienceStood;
                audienceStood = j;
            }
            audienceStood += input[j] - '0';
        }
        cout << friendsNeeded << endl;
    }

    return 0;
}
