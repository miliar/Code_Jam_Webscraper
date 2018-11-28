 #include <bits/stdc++.h>
 using namespace std;
 
 bool flag;
 
 string compute(char a, char b) {
     if (a == '1' && b == '1') return "1";
        else if (a == '1' && b == 'i') return "i";
        else if (a == '1' && b == 'j') return "j";
        else if (a == '1' && b == 'k') return "k";
        else if (a == 'i' && b == '1') return "i";
        else if (a == 'i' && b == 'i') { flag = !flag; return "1";  }
        else if (a == 'i' && b == 'j') return "k";
        else if (a == 'i' && b == 'k') { flag = !flag; return "j";  }
        else if (a == 'j' && b == '1') return "j";
        else if (a == 'j' && b == 'i') { flag = !flag; return "k";  }
        else if (a == 'j' && b == 'j') { flag = !flag;return "1";  }
        else if (a == 'j' && b == 'k') return "i";
        else if (a == 'k' && b == '1') return "k";
        else if (a == 'k' && b == 'i') return "j";
        else if (a == 'k' && b == 'j') { flag = !flag;return "i";  }
        else if (a == 'k' && b == 'k') { flag = !flag;return "1";  }
 }
 
 int main(int argc, char** argv) {
     int tests;
     string in;
     cin >> tests;
     for (int test = 1; test <= tests; test++) {
         int l,x;
         string complete;
         cin >> l >> x >> in;
         flag = false;
         for (int i = 0; i < x; i++)
             complete.append(in);
         while (complete[0] != 'i' && complete.length() > 3)
             complete.replace(0, 2, compute(complete[0], complete[1]));
         while (complete[1] != 'j' && complete.length() > 3)
             complete.replace(1, 2, compute(complete[1], complete[2]));
         while (complete.length() > 3)
             complete.replace(2, 2, compute(complete[2], complete[3]));
         
         if (complete == "ijk" && !flag)
            cout << "Case #" << test << ": YES" << endl;
        else
            cout << "Case #" << test << ": NO" << endl;
     }
     return 0;
 }