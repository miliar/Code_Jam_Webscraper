#include <iostream>
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>

int main(void)
{
    std::size_t cases = 0;

    scanf("%d\n", &cases);

    for (int i = 0; i < cases; i++) {
        int row1 = 0;
        scanf("%d\n", &row1);
        std::set<int> s1;
        for (int j = 1; j < 5; j++) {
            int a,b,c,d;
            scanf("%d %d %d %d\n", &a,&b,&c,&d);
            if (j == row1) {
                s1.insert(a);
                s1.insert(b);
                s1.insert(c);
                s1.insert(d);
            }
        }

        int row2 = 0;
        scanf("%d\n", &row2);
        std::set<int> s2;
        for (int j = 1; j < 5; j++) {
            int a,b,c,d;
            scanf("%d %d %d %d\n", &a,&b,&c,&d);
            if (j == row2) {
                s2.insert(a);
                s2.insert(b);
                s2.insert(c);
                s2.insert(d);
            }
        }

        std::vector<int> inter(8);
        std::vector<int>::iterator it;

        it = std::set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), inter.begin());
        inter.resize(it-inter.begin());

        if (inter.empty()) {
            std::cout << "Case #" << i+1 << ": " << "Volunteer cheated!";
        } else if (inter.size() > 1) {
            std::cout << "Case #" << i+1 << ": " << "Bad magician!";
        } else {
            std::cout << "Case #" << i+1 << ": " << inter[0];
        }

        if (i < cases-1) {
            std::cout << std::endl;
        }
    }

    return 0;
}
