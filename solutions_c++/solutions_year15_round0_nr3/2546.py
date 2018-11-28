#include <vector>
#include <iostream>
#include <stdint.h>

class Quaternion {
    // 0x00 = 1
    // 0x01 = i
    // 0x02 = j
    // 0x03 = k
    // 0x04 = negative
    uint8_t value;

public:
    Quaternion() : value(0) { }
    Quaternion(uint8_t value) : value(value) { }
    void reset() { value = 0; }

    static Quaternion i() { return 0x01; }
    static Quaternion j() { return 0x02; }
    static Quaternion k() { return 0x03; }

    Quaternion operator-(const Quaternion& q) const {
        return q.value ^ 0x04;
    }

    bool operator==(const Quaternion& other) const {
        return value == other.value;
    }

    bool operator!=(const Quaternion& other) const {
        return value != other.value;
    }

    Quaternion& operator*=(const Quaternion& q) {
        uint8_t sign = (value & 0x04) ^ (q.value & 0x04);
        switch (((value & 0x03) << 4) | (q.value & 0x03)) {
            // 1 * q
            case 0x00: value = 0x00; break; // 1
            case 0x01: value = 0x01; break; // i
            case 0x02: value = 0x02; break; // j
            case 0x03: value = 0x03; break; // k
            // i * q
            case 0x10: value = 0x01; break; // i
            case 0x11: value = 0x04; break; // -1
            case 0x12: value = 0x03; break; // k;
            case 0x13: value = 0x06; break; // -j
            // j * q
            case 0x20: value = 0x02; break; // j
            case 0x21: value = 0x07; break; // -k
            case 0x22: value = 0x04; break; // -1
            case 0x23: value = 0x01; break; // i
            // k * q
            case 0x30: value = 0x03; break; // k
            case 0x31: value = 0x02; break; // j
            case 0x32: value = 0x05; break; // -i
            case 0x33: value = 0x04; break; // -1
        }
        value ^= sign;
        return *this;
    }

    friend Quaternion operator*(const Quaternion& qa, const Quaternion& qb) {
        Quaternion result = qa;
        result *= qb;
        return result;
    }

    friend std::istream& operator>>(std::istream& stream, Quaternion& q) {
        char c;
        stream >> c;
        switch (c) {
        case '1': q.value = 0x00; break;
        case 'i': q.value = 0x01; break;
        case 'j': q.value = 0x02; break;
        case 'k': q.value = 0x03; break;
        }
        return stream;
    }

    friend std::ostream& operator<<(std::ostream& stream, const Quaternion& q) {
        if (q.value & 0x04)
            stream << '-';
        switch (q.value & 0x03) {
        case 0x00: stream << '1'; break;
        case 0x01: stream << 'i'; break;
        case 0x02: stream << 'j'; break;
        case 0x03: stream << 'k'; break;
        }
        return stream;
    }
};

int main() {
    int T;
    std::cin >> T;
    std::vector<Quaternion> L;
    // contests make the most horrible code, no validations, etc.
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        size_t Lcount, Xcount;
        std::cin >> Lcount >> Xcount;
        L.resize(Lcount);
        Quaternion fullL;
        for (size_t i = 0; i < Lcount; ++i) {
            std::cin >> L[i];
            fullL *= L[i];
        }
        size_t count = Lcount * Xcount;
        Quaternion curI, curJ, curK;
        size_t idxI = 0;
        size_t leftI = count;
        while (leftI > 2) {
            if (idxI == Lcount)
                idxI = 0;
            curI *= L[idxI];
            if (curI == Quaternion::i()) {
                curJ.reset();
                size_t idxJ = idxI + 1;
                size_t leftJ = leftI - 1;
                while (leftJ > 1) {
                    if (idxJ == Lcount)
                        idxJ = 0;
                    curJ *= L[idxJ];
                    if (curJ == Quaternion::j()) {
                        //std::cout << "... verifying k:" << std::endl;
                        curK.reset();
                        size_t idxK = idxJ + 1;
                        size_t leftK = leftJ - 1;
                        while (leftK) {
                            if (idxK == Lcount) {
                                // leftK is divisible by Lcount
                                // means we can multiply by fullL
                                size_t fullCount = leftK / Lcount;
                                //std::cout << "... leftK = " << leftK << std::endl;
                                //std::cout << " Lcount = " << Lcount << std::endl;
                                //std::cout << "... fullCount = " << fullCount << std::endl;
                                Quaternion power = fullL;
                                while (fullCount) {
                                    if (fullCount & 1) {
                                        //std::cout << "... " << curK << " * " << power;
                                        curK *= power;
                                        //std::cout << " = " << curK << std::endl;
                                    }
                                    fullCount >>= 1;
                                    power *= power;
                                }
                                break;
                            }
                            //std::cout << "... " << curK << " * " << L[idxK];
                            curK *= L[idxK];
                            //std::cout << " = " << curK << std::endl;
                            --leftK;
                            ++idxK;
                        }
                        if (curK == Quaternion::k())
                            goto found;
                    }
                    --leftJ;
                    ++idxJ;
                }
            }
            --leftI;
            ++idxI;
        }
    not_found:
        std::cout << "Case #" << caseNum << ": NO" << std::endl;
        continue;
    found:
        std::cout << "Case #" << caseNum << ": YES" << std::endl;
    }
    return 0;
}
