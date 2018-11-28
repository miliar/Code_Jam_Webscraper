//
//  InfiniteHouseOfPancakes.cpp
//  Infinite House of Pancakes
//

#include <iostream>
#include <fstream>

int main(int argc, const char * argv[]) {
    int T, X;
    int diners;
    int D[100001];
    int TT[100001];
    int T2[100001];
    int TFINAL1[100001];
    int TFINAL2[100001];
    int max;
    int index;
    int tracker;
    int time;
    int temp;
    int tracker2;
    freopen("/Users/Michael/Desktop/B-small-attempt6.in", "r", stdin);
    std::ofstream out("/Users/Michael/Desktop/output");
    int count = 0;
    scanf("%i", &T);
    X = T;
    while (T--) {
        tracker = 0;
        time = 0;
        tracker2 = 0;
        scanf("%i", &diners);
        for (int i = 0; i < diners; i++) {
            scanf("%i", &D[i]);
        }
        while (tracker == 0) {
            max = 0;
            for (int i = 0; i < diners; i++) {
                if (D[i] > max) {
                    max = D[i];
                    index = i;
                }
                TT[tracker2] = max + time;
            }
            if (max < 4) {
                tracker++;
            }
            else {
                if (D[index] / 3 == 3) {
                    temp = D[index] / 3;
                    D[index] -= temp;
                    D[diners] = temp;
                }
                else if (D[index] / 2 == 3) {
                    temp = D[index] / 2;
                    D[index] -= temp;
                    D[diners] = temp;
                }
                else if (D[index] % 2 == 0) {
                    temp = D[index] / 2;
                    D[index] -= temp;
                    D[diners] = temp;
                }
                else {
                    temp = D[index] / 2;
                    D[index] -= temp;
                    D[diners] = temp + 1;
                }
                diners++;
                time++;
                tracker2++;
            }
        }
        
        temp = TT[0];
        for (int i = 1; i < tracker2 + 1; i++) {
            if (TT[i] < temp) {
                temp = TT[i];
            }
        }
        
        TFINAL1[count] = temp;
        
        count++;
    }
    fclose (stdout);
    
    
    
    
    
    
    
    freopen("/Users/Michael/Desktop/B-small-attempt6.in", "r", stdin);
    count = 0;
    scanf("%i", &T);
    while (T--) {
        tracker = 0;
        time = 0;
        tracker2 = 0;
        scanf("%i", &diners);
        for (int i = 0; i < diners; i++) {
            scanf("%i", &D[i]);
        }
        while (tracker == 0) {
            max = 0;
            for (int i = 0; i < diners; i++) {
                if (D[i] > max) {
                    max = D[i];
                    index = i;
                }
                T2[tracker2] = max + time;
            }
            if (max < 4) {
                tracker++;
            }
            else {
                if (D[index] % 2 == 0) {
                    temp = D[index] / 2;
                    D[index] -= temp;
                    D[diners] = temp;
                }
                else {
                    temp = D[index] / 2;
                    D[index] -= temp;
                    D[diners] = temp + 1;
                }
                diners++;
                time++;
                tracker2++;
            }
        }
        
        temp = T2[0];
        for (int i = 1; i < tracker2 + 1; i++) {
            if (T2[i] < temp) {
                temp = T2[i];
            }
        }
        
        TFINAL2[count] = temp;
        
        count++;
    }
    
    
    for (int w = 1; w < X + 1; w++) {
        out << "Case #" << w << ": ";
        if (TFINAL1[w - 1] < TFINAL2[w - 1]) {
            temp = TFINAL1[w - 1];
        }
        else {
            temp = TFINAL2[w - 1];
        }
        out << temp << "\n";
    }
    
    
    out.close();
    fclose (stdout);
    
    
    
    
    return 0;
}