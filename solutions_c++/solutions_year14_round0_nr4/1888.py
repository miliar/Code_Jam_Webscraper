#include <iostream>
#include <list>
using namespace std;

int main() 
{
    int T;
    cin >> T;
    for (int t=1; t<=T; t++)
    {
        int N, y, z;
        double buffer;
        cin >> N;
        list<double> naomi1;
        list<double> ken1;
        
        for (int i=0; i<N; i++) {
            cin >> buffer;
            naomi1.push_back(buffer);
        }
        for (int i=0; i<N; i++) {
            cin >> buffer;
            ken1.push_back(buffer);
        }
        naomi1.sort();
        ken1.sort();
        
        list<double> naomi2 = naomi1;
        list<double> ken2 = ken1;

        y = 0;
        while (!naomi1.empty() && !ken1.empty()) {
            while (!naomi1.empty() && !ken1.empty() && naomi1.back() < ken1.back())
                ken1.pop_back();
            if (!naomi1.empty() && !ken1.empty() && naomi1.back() > ken1.back())
                y++;
            ken1.pop_back();
            naomi1.pop_back();
        }
        
        z = 0;
        while (!naomi2.empty() && !ken2.empty()) {
            while (!naomi2.empty() && !ken2.empty() && naomi2.front() > ken2.front())
                ken2.pop_front();
            if (!naomi2.empty() && !ken2.empty() && naomi2.front() < ken2.front())
                z++;
            ken2.pop_front();
            naomi2.pop_front();
        }
        z = N - z;

        cout << "Case #" << t << ": " << y << " " << z << endl;

    }
}