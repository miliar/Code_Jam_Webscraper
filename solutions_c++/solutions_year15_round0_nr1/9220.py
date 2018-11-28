#include <stdio.h>
#include <string>
#include <iostream>
#include <typeinfo>

using namespace std;

int main()
{
    //freopen( "A-large.in", "r", stdin );
	//freopen( "output.txt", "w", stdout );
    int t;

    cin >> t;
    int n = t;
    while (t--) {
        int smax;
        string audience;
        //int arr[1005];
        cin >> smax >> audience;
        int total_people = 0;
        int people_required = 0;
        for (int i = 0; i <= smax; i++) {
            if (total_people < i) {
                people_required += i - total_people;
                total_people += i - total_people;
            }
            int people = audience[i] - '0';
            total_people += people;
        }
        cout << "Case #" << (n - t) << ": " << people_required << endl;
        //cout << smax << " " << audience;
    }
    return 0;
}
