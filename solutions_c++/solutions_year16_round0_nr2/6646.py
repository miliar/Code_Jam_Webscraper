#include <iostream>
using namespace std;

int needToFlip(bool ar[100], int size);
void flip(bool (&ar)[100], int j);

int main(){
  int t;
  string n;
  cin >> t;
  for (int c = 1; c <= t; c++){
	bool ar[100];
    cin >> n;
	for (int i = 0; i < n.length(); i++){
		if (n[i] == '-'){
			ar[i] = false;
		}
		else{
			ar[i] = true;
		}
	}
		
	int cont = 0;
	int ntf = needToFlip(ar, n.length());
	while (ntf != -1){
		cont++;
		flip(ar, ntf);
		
		ntf = needToFlip(ar, n.length());
	}
	
	cout << "Case #" << c << ": " << (cont) << endl;
  }
}

int needToFlip(bool ar[100], int size){
	if (!ar[0]){
		for (int i = 1; i < size; i++){
			if (ar[i]){
				return i - 1;
			}
		}
		return size - 1;
	}
	else{
		for (int i = 1; i < size; i++){
			if (!ar[i]){
				return i - 1;
			}
		}
		return - 1;
	}
}

void flip(bool (&ar)[100], int j){
	for (int i = 0; i <= j; i++){
		ar[i] = !ar[i];
	}
}
