#include <math.h>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

static int Isqrt(int num)
{
    if (0 == num) { return 0; }  // Avoid zero divide
    int n = (num / 2) + 1;       // Initial estimate, never low
    int n1 = (n + (num / n)) / 2;
    while (n1 < n)
    {
        n = n1;
        n1 = (n + (num / n)) / 2;
    } // end while
    return n;
} // end Isqrt()

int isPallindrome (int num) {
     int n, digit, rev = 0;
     n = num;
     do {
         digit = num%10;
         rev = (rev*10) + digit;
         num = num/10;
     } while (num!=0);
     if (n == rev)
       return 1;
     else
       return 0;
}

int main () {
  string line;
  ifstream infile ("C-small-attempt3.in");
  ofstream outfile ("C-small-attempt3.out");
  if (infile.is_open())
  {
    getline (infile,line);
    int num = atoi(line.c_str());
    for (int i = 0; i < num; i++) {
        getline (infile,line);
        char a[16];
        char b[16];
        int j = 0;
        while (line.c_str()[j] != ' ') {
            a[j] = line.c_str()[j];
            j++;
        }
        a[j] = '\0';
        j++;
        int k = 0;
        while( (line.c_str()[j] == '0') ||
               (line.c_str()[j] == '1') ||
               (line.c_str()[j] == '2') ||
               (line.c_str()[j] == '3') ||
               (line.c_str()[j] == '4') ||
               (line.c_str()[j] == '5') ||
               (line.c_str()[j] == '6') ||
               (line.c_str()[j] == '7') ||
               (line.c_str()[j] == '8') ||
               (line.c_str()[j] == '9') ) {
            b[k] = line.c_str()[j];
            k++;
            j++;
        }
        b[k] = '\0';
        int start = atoi(a);
        int end = atoi(b);
//        cout << start << " " << end << endl;
        int count = 0;
        for (int x = start; x <= end; x++) {
            if (Isqrt(x)*Isqrt(x) == x && isPallindrome(x) && isPallindrome(Isqrt(x))) {
                count++;
                cout << x << " ";
            }
        }
        cout << endl;
        outfile << "Case #" << i+1 << ": " << count;
        if (i+1 != num) outfile << endl;
    }
  }

  else cout << "Unable to open file"; 
  system("PAUSE");
  return 0;
}
