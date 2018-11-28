#include <iostream>
#include <cstring>
#include <list>
int main() {
    int t;
    char s1[10001],s2[10001];
    std::cin >> t;
    for (int ttt = 1; ttt <= t; ttt++) {
        std::cin >> s1;
        int len = strlen(s1);
        std::list<char> ll;
        ll.push_back(s1[0]);
        for (int i = 1; i < len; i++) {
            if (s1[i] >= ll.front())
                ll.push_front(s1[i]);
            else
                ll.push_back(s1[i]);
        }
        for (int i = 0; i < len; i++) {
            s2[i] = ll.front();
            ll.pop_front();
        }
        s2[len] = '\0';
        std::cout << "Case #" << ttt << ": " << s2 << std::endl;
    }
    return 0;
}
