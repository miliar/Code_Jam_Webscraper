#include <iostream>

using namespace std;

int main()
{
    //Taking the number of test cases as the input
    int T;
    cin>>T;
    //Checking for each test case
    for (int i=0; i<T; i++) {
        int ans1, ans2, grid1[4][4], grid2[4][4], temp[4], count=0, x;
        //Taking the first set of numbers and the answer as the input
        cin>>ans1;
        for (int j=0; j<4; j++) {
            for (int k=0; k<4; k++) {
                cin>>grid1[j][k];
            }
        }
        //Temporarily storing the first answer's possible values in an array
        for (int a=0; a<4; a++) {
            temp[a] = grid1[ans1-1][a];
        }
        //Taking the second set of numbers and the answer as the input
        cin>>ans2;
        for (int j=0; j<4; j++) {
            for (int k=0; k<4; k++) {
                cin>>grid2[j][k];
            }
        }
        //Checking for common values
        for (int j=0; j<4; j++) {
            for (int k=0; k<4; k++) {
                if (temp[j]==grid2[ans2-1][k]) {
                    count++;
                    x = temp[j];
                }
            }
        }
        //Output
        if (count==0) {
            cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
        }
        else if (count==1) {
            cout<<"Case #"<<i+1<<": "<<x<<endl;
        }
        else {
            cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
        }
    }
    return 0;
}
