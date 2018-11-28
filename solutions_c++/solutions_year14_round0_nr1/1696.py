#include <iostream>
using namespace std;
int main()
{
    long int t;
    cin >> t;
    for(long int q = 1;q<=t;++q){
        // input
        int ans1;
        int counter = 0;
        cin >> ans1;
        ans1--;
        int arr[4][4];
        int answer[4];
        for(int i=0;i<4;++i)
            for(int j=0;j<4;++j)
                cin >> arr[i][j];
        int ans2;
        cin >> ans2;
        ans2--;
        int arr2[4][4];
        for(int i=0;i<4;++i)
            for(int j=0;j<4;++j)
                cin >> arr2[i][j];
        // calculations
        int num;
        for(int i=0;i<4;++i)
            answer[i] = arr[ans1][i];
        for(int i=0;i<4;++i)
        {
            for(int j=0;j<4;++j)
            {
                if(answer[i]==arr2[ans2][j])
                {
                    counter++;
                    num=answer[i];
                }
            }
        }
        if(counter==1)
            cout << "Case #" << q << ": " << num << endl;
        else if(counter == 0)
            cout << "Case #" << q << ": Volunteer cheated!" << endl;
        else
            cout << "Case #" << q << ": Bad magician!" <<endl;
    }
    return 0;
}
