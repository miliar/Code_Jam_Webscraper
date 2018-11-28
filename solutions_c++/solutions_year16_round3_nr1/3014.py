#include <iostream>

using namespace std;

void max_heapify(int P[], char char_P[], int i, int n)
{
    int j, temp;
    char temp_char;
    temp = P[i];
    temp_char = char_P[i];
    j = 2 * i;
    while (j <= n)
    {
        if (j < n && P[j+1] >= P[j])
            j = j + 1;
        if (temp >= P[j])
            break;
        else if (temp < P[j])
        {
            P[j / 2] = P[j];
            char_P[j/2] = char_P[j];
            j = 2 * j;
        }
    }
    P[j/2] = temp;
    char_P[j/2] = temp_char;
    return;
}
void create_max_heap(int P[],char char_P[], int n)
{
    int i;
    for(i = n/2; i >= 0; i--)
    {
        max_heapify(P, char_P, i, n);
    }
}

int main() {
    int T;
    cin >> T;
    for(int _ = 0; _ < T; _++) {
        int N;
        cin >> N;
        int *P = new int[N];
        char *char_P = new char[N];
        for(int i = 0; i < N; i++) {
            int temp;
            cin >> temp;
            P[i] = temp;
            char_P[i] = (char)(65 + i);
        }

        create_max_heap(P, char_P, N - 1);

        //cout << P[0] << " " << P[1] << " " << P[2] << endl;
        //cout << char_P[0] << " " << char_P[1] << " " << char_P[2];

        cout << "Case #" << _ + 1 << ": ";
        while(1) {
            //cout << "P[0]: " << P[0] << endl;
            if (P[0] == 1 && P[1] == 1 && P[2] == 1) {
                cout << char_P[0];
                cout << " ";
                cout << char_P[1] << char_P[2];
                break;
            }
            else if (P[0] == 1 && P[1] == 1) {
                cout << char_P[0] << char_P[1] << " ";
                break;
            }
            else {
                cout << char_P[0];
                P[0]--;
                max_heapify(P, char_P, 0, N - 1);
                //cout << endl;
                //cout << P[0] << " " << P[1] << " " << P[2] << endl;
                //cout << char_P[0] << " " << char_P[1] << " " << char_P[2];
                cout << char_P[0];
                P[0]--;
                max_heapify(P, char_P, 0, N - 1);
                //cout << P[0] << " " << P[1] << " " << P[2] << endl;
                //cout << char_P[0] << " " << char_P[1] << " " << char_P[2];
            }
            cout << " ";
            if (P[0] == 0)
                break;
        }
        cout << endl;

    }
}
