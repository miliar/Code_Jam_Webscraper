#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    ifstream in("input.txt");
	ofstream out("output.txt");
    int Tin, testcase;
    int arr[1001]={0,};
    arr[1] = 1;
    arr[4] = 1;
    arr[9] = 1;
    arr[121] = 1; //11
    arr[484] = 1; //22

    in>>Tin;
    for(testcase = 1 ; testcase <= Tin ; testcase++){
        int A, B;
        int ans = 0;
        in>>A>>B;
        for(; A <= B ; A++){
            if(arr[A]==1) ans++;
        }
        out<<"Case #"<<testcase<<": "<<ans<<endl;
    }

    in.close();
    out.close();
    return 0;
}
