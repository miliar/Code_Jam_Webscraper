#include <iostream>

using namespace std;

void output(int result, int i);
void input(int &one, int &two, int &three, int &four);
void checkhelper(int one, int two, int three, int four, int &result);
void checker(int one, int two, int three, int four, int &result);

int main() {
    int totalrounds;
    cin >> totalrounds;
    int one = 0;
    int two = 0;
    int three = 0;
    int four = 0;
    int question = 0;
    int result = 0;
    for(int i = 0; i < totalrounds; i++) {
        input(one, two, three, four);
        checker(one, two, three, four, result);
        output(result, i);
	result = 0;
    }
    return 0;
}

void checkhelper(int one, int two, int three, int four, int &result) {
        for(int j = 0; j < 4; j++) {
            int maybe = 0;
            cin >> maybe;
            if(maybe == one) {
		if(result != 0) {
		result = -2;
		}
		else {
                result = one;
		}
            }
            if(maybe == two) {
                if(result != 0) {
                    result = -2;
                }
                else {
                    result = maybe;
                }
            }
            if(maybe == three) {
                if(result != 0) {
                    result = -2;
                }
                else {
                    result = maybe;
                }
            }
            if(maybe == four) {
                if(result != 0) {
                    result = -2;
                }
                else {
                    result = maybe;
                }
            }
            //if there wasn't a match
        }
	if(result == 0) {
		result = -1;
	}
        return;
}

void checker(int one, int two, int three, int four, int &result) {
    int garbage = 0;
    int position;
    cin >> position;
    if(position == 1) {
        checkhelper(one, two, three, four, result);
        for(int j = 0; j < 12; j++) {
            cin >> garbage;
        }
    }
    else if(position == 2) {
        for(int j = 0; j < 4; j++) {
            cin >> garbage;
        }
        checkhelper(one, two, three, four, result);
        for(int j = 0; j < 8; j++) {
            cin >> garbage;
        }
    }
    else if(position == 3) {
        for(int j = 0; j < 8; j++) {
            cin >> garbage;
        }
        checkhelper(one, two, three, four, result);
        for(int j = 0; j < 4; j++) {
            cin >> garbage;
        }
    }
    else {
        for(int j = 0; j < 12; j++) {
            cin >> garbage;
        }
        checkhelper(one, two, three, four, result);
    }
    return;
}

void input(int &one, int &two, int &three, int &four) {
    int position = 0;
    int garbage = 0;
    cin >> position;
    if(position == 1) {
        cin >> one >> two >> three >> four;
        for(int j = 0; j < 12; j++) {
            cin >> garbage;
        }
    }
    else if(position == 2) {
        for(int j = 0; j < 4; j++) {
            cin >> garbage;
        }
        cin >> one >> two >> three >> four;
        for(int j = 0; j < 8; j++) {
            cin >> garbage;
        }
    }
    else if(position == 3) {
        for(int j = 0; j < 8; j++) {
            cin >> garbage;
        }
        cin >> one >> two >> three >> four;
        for(int j = 0; j < 4; j++) {
            cin >> garbage;
        }
    }
    else {
        for(int j = 0; j < 12; j++) {
            cin >> garbage;
        }
        cin >> one >> two >> three >> four;
    }
    return;
}

void output(int result, int i) {
    cout << "Case #" << i + 1 << ": ";
    if(result == -1) {
        cout << "Volunteer cheated!\n";
    }
    else if(result == -2) {
        cout << "Bad magician!\n";
    }
    else {
        cout << result << "\n";
    }
}
