#include <iostream>
#include <string>

//#define DEBUG 1

class ActuralValue {
    public:
        ActuralValue(int sign, char value);
        ActuralValue& setValue(char value);
        ActuralValue& setSign(char value);
        ActuralValue& opposite();
        ActuralValue operator*(ActuralValue other);
        bool operator ==(ActuralValue& other);
        void print();
    private:
        int sign;
        char value;
};

ActuralValue::ActuralValue(int sign, char value) {
    this->sign = sign;
    this->value = value;
}

bool ActuralValue::operator ==(ActuralValue& other) {
    return sign == other.sign && value == other.value;
}

ActuralValue& ActuralValue::setValue(char v) {
    value = v;
    return *this;
}

ActuralValue& ActuralValue::setSign(char s) {
    sign = s;
    return *this;
}

ActuralValue& ActuralValue::opposite() {
    sign = -sign;
    return *this;
}


ActuralValue ActuralValue::operator*(ActuralValue other) {
    ActuralValue result(sign * other.sign, '1');

    if (value == '1') return result.setValue(other.value);
    if (other.value == '1') return result.setValue(value);

    if (value == other.value) return result.opposite();

    if (value == 'i' && other.value == 'j') return result.setValue('k');
    if (value == 'i' && other.value == 'k') return result.setValue('j').opposite();
    if (value == 'j' && other.value == 'i') return result.setValue('k').opposite();
    if (value == 'j' && other.value == 'k') return result.setValue('i');
    if (value == 'k' && other.value == 'i') return result.setValue('j');
    if (value == 'k' && other.value == 'j') return result.setValue('i').opposite();
    return result;
}

void ActuralValue::print() {
#ifdef DEBUG
    std::cout << (sign == -1 ? "-" : "") << value << " ";
#endif
}


static ActuralValue createAV(int sign, char value) {
    ActuralValue av(sign, value);
    return av;
}

int main(int argc, char *argv[]) {
    int T;
    std::string s;
    std::cin >> T;
    for (int t = 0; t < T; ++t) {
        long l, x;
        std::cin >> l >> x;
        std::cin >> s;
        int i;
        ActuralValue avI(1, 'i');
        ActuralValue avJ(1, 'j');
        ActuralValue avK(1, 'k');
        ActuralValue avMinusOne(-1, '1');

        ActuralValue current(1, '1');
        int achievement = 0;
        for (i = 0; i < l * x; i++) {
            current = current * createAV(1, s[i % l]);
            current.print();
            if (current == avI) {
                i++;
                achievement++;
                break;
            }
        }
        for (; i < l * x; i++) {
            current = current * createAV(1, s[i % l]);
            current.print();
            if (current == avK) {
                i++;
                achievement++;
                break;
            }
        }
        for (; i < l * x; i++) {
            current = current * createAV(1, s[i % l]);
            current.print();
            if (current == avMinusOne) {
                i++;
                achievement++;
                break;
            }
        }

        for (; i < l * x; i++) {
            current = current * createAV(1, s[i % l]);
            current.print();
        }

        if (current == avMinusOne) {
            achievement++;
        }
        std::cout << "Case #" << t + 1 << ": " << ((achievement == 4) ? "YES" : "NO") << std::endl;
    }
    return 0;
}
