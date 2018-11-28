#include <iostream>

using namespace std;

int main()
{
    int T;

    cin >> T;
    for(int t=1; t<=T; t++) {
        string s, news;
        cin >> s;
        news.insert(news.begin(), s.at(0));
        for(int i=1; i<s.length(); i++) {
            if (s.at(i) >= news.at(0)) news.insert(news.begin(), s.at(i));
            else news.push_back(s.at(i));
        }
        cout << "Case #" << t << ": " << news << endl;
    }
    return 0;
}
