#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

const int MAX = 1000000+2;

int parent[MAX];
bool seen[MAX];

long reverse(long number){
    long r = 0;

    while (number != 0){
      r = r * 10;
      r = r + number%10;

      number = number/10;
   }

   return r;
}


int main(){
    ifstream cin("input.txt");
    ofstream cout("output.txt");

    for (int i = 0; i < MAX; i++){
        parent[i] = -1;
        seen[i] = false;
    }

    int a = 1000001;

    queue<unsigned long long> q;
    q.push(1);
    parent[1] = -1;

    int tot = 0;

    while (true){
        tot++;
        unsigned long long top = q.front();
        if (top == a)
            break;

        q.pop();

        unsigned long long l = reverse(top);
        unsigned long long r = top+1;

        if (l > top){
            if (!seen[l]){
                q.push(l);
                parent[l] = top;
                seen[l] = true;
            }
        }

        if (!seen[r]){
            parent[r] = top;
            q.push(r);
            seen[r] = true;
        }
    }

    int n;
    cin >> n;
    for (int k = 1; k <= n; k++){
        int a;
        cin >> a;


        int steps = 1;
        while (parent[a] != -1){
            steps++;
            a = parent[a];
        }

        cout << "Case #" << k << ": " << steps << endl;
    }
    return 0;
}
