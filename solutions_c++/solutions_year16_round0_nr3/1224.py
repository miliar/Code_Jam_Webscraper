/**
I used to following Magma code to generate the answers
**/

n := 2147483649;
it := 0;
SetLogFile("C-large-out.txt");
while(n le 4294967295 and it lt 500) do
	succes := true;
	//print Intseq(n,2);
	list := [0 : y in [1..9]];
	for i in [2..10] do
		b := Seqint(Intseq(n,2),i);
		if(not IsPrime(b)) then
			k := Factorization(b)[1][1];
			//print "Base getal ", b, "in basis ", i, "met deler ", k;
			wut := i-1;
			list[wut] := k;
		else
			succes := false;
			break;
		end if;
	end for;
	if(succes) then
		m := Reverse(Intseq(n,2));
		for j in [1..32] do
			print(m[j]);
		end for;
		//print Intseq(n,2);
		for j in [1..9] do
			print list[j];
		end for;
		it +:= 1;
	end if;
	n +:= 2;
end while;
UnsetLogFile();

/* Then I used a c++ program to format the logfile in the required format.

/*
#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cout << "Case #1:" << endl;
    int64_t n;
    while(cin >> n, n != 0){
        cout << n;
        for(int i = 0; i < 31; i++){
            cin >> n;
            cout << n;
        }
        for(int i = 0; i < 9; i++){
            cin >> n;
            cout << " " << n;
        }
        cout << endl;
    }
    return 0;
}
*/
