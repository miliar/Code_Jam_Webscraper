#include <iostream>


int main() {
    int T;
    std :: cin >> T;
    for (int cas = 1; cas <= T; ++ cas) {
        int x;
        std :: cin >> x;
        int a[4], b[4];
        for (int i = 0; i < 4; ++ i)
            for (int j = 0; j < 4; ++ j)
                if (i + 1 == x)
                    std :: cin >> a[j];
                else {
                    int t;
                    std :: cin >> t;
                }
        std :: cin >> x;
        for (int i = 0; i < 4; ++ i)
            for (int j = 0; j < 4; ++ j)
                if (i + 1 == x)
                    std :: cin >> b[j];
                else {
                    int t;
                    std :: cin >> t;
                }
        int num = 0;
        for (int i = 0; i < 4; ++ i)
            for (int j = 0; j < 4; ++ j)
                if (a[i] == b[j])
                    ++ num;
        std :: cout << "Case #" << cas << ": ";
        if (0 == num)
            std :: cout << "Volunteer cheated!\n";
        else if (1 < num)
            std :: cout << "Bad magician!\n";
        else {
            for (int i = 0; i < 4; ++ i)
                for (int j = 0; j < 4; ++ j)
                    if (a[i] == b[j])
                        std :: cout << a[i] << std :: endl;
        }
    }
    return 0;
}
