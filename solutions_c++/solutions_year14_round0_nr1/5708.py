# include <iostream>

using namespace std;

long long int p, q;

long long int a[8][8], b[8][8], tfo[32];

void read ()
{

    long long int i, j, br = 0, ans, k, t;
br = ans = 0;
scanf ("%I64d", &p);
for (i = 0; i < 4; i ++)
for (j = 0; j < 4; j ++)
scanf ("%I64d", &a[i][j]);

scanf ("%I64d", &q);
for (i = 0; i < 4; i ++)
for (j = 0; j < 4; j ++)
scanf ("%I64d", &b[i][j]);
}

int main ()
{
long long int i, j, br = 0, ans, k, t;
scanf ("%I64d", &t);
for (k = 0; k < t; k ++)
{
read ();
br = ans = 0;

for (i = 0; i < 4; i ++)
{
tfo[a[p - 1][i]] ++;
tfo[b[q - 1][i]] ++;
}

for (i = 1; i <= 16; i ++)
if (tfo[i] == 2)
{
br ++;
ans = i;
}
cout << "Case #" << k + 1 << ": ";
if (br == 0) printf ("Volunteer cheated!\n");
else if (br == 1) cout << ans << endl;
else printf ("Bad magician!\n");
for (i = 0; i < 17; i ++)
tfo[i] = 0;
}
return 0;
}
